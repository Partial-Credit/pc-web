from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.models import Permission
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.contrib import messages
from .models import Member
from .forms import MemberForm, FullMemberForm

@login_required
@permission_required('users.officer', raise_exception=True)
def add(request):

    if request.method == 'POST':
        form = FullMemberForm(request.POST, request.FILES, None)

        if form.is_valid():
            instance = form.save()

            # Add all applicable permissions
            view_permission = Permission.objects.get(codename='view_member')
            modify_permission = Permission.objects.get(codename='change_member')
            instance.user_permissions.add(view_permission, modify_permission)

            # Check if officer permission should be added
            if len(instance.position) >= 1:
                officer_permission = Permission.objects.get(codename='officer')
                instance.user_permissions.add(officer_permission)

            instance.save()

            messages.success(request, "Member added successfully")
            next = request.POST.get('next', "/")
            return redirect('users:view_all')
        else:
            return HttpResponse("Form failed to validate.", status=403)
    else:
        form = FullMemberForm()
        return render(request, 'users/add.html', {"form": form, "button_text": "Add"})



@login_required
@permission_required('users.officer', raise_exception=True)
def remove(request, member_id):
    instance = get_object_or_404(Member, pk=member_id)

    # Set is_active to False instead of deleting. This keeps the data around
    # so references to the user object such as arranger credit can be maintained.
    # The assumed use case for removing a user is if a member leaves the group
    # early before they graduate.
    instance.is_active = False


    instance.current_member = False

    # Remove officer perms if this person has them
    if len(instance.position) >= 1:
        officer_permission = Permission.objects.get(codename='officer')
        instance.user_permissions.remove(officer_permission)
        instance.position = None

    instance.save()

    return redirect('users:view_all')




@login_required
@permission_required('users.change_member', raise_exception=True)
def edit(request, member_id):
    instance = get_object_or_404(Member, pk=member_id)

    # Check if user is modifying themselves
    if instance.username == request.user.username:
        # User is modifying their own object

        if request.method == 'POST':
            if request.user.has_perm('users.officer'):
                officer=True
            else:
                officer=False

            if officer:
                form = FullMemberForm(request.POST, request.FILES, instance=instance)
            else:
                form = MemberForm(request.POST, request.FILES, instance=instance)

            if form.is_valid():
                instance = form.save()

                if officer:
                    # Check adding or removing permissions
                    officer_permission = Permission.objects.get(codename='officer')
                    print(instance.position)
                    if len(instance.position) >= 1:
                        instance.user_permissions.add(officer_permission)
                        instance.save()
                    else:
                        instance.user_permissions.remove(officer_permission)
                        instance.save()

                messages.success(request, "Member updated successfully")
                return redirect('users:view_all')

        else: #GET request
            if request.user.has_perm('users.officer'):
                form = FullMemberForm(instance=instance)
            else:
                form = MemberForm(instance=instance)

            context = {
                "form": form,
                "member_id": instance.id,
                'button_text': 'Update Member',
            }
            return render(request, 'users/edit.html', context)

    # If user isn't trying to change their own object check if they have permission to modify others
    elif request.user.has_perm('users.officer'):
        # Modify other user
        if request.method == 'POST':
            form = FullMemberForm(request.POST, request.FILES, instance=instance)
            if form.is_valid():
                instance = form.save()
                officer_permission = Permission.objects.get(codename='officer')
                if len(instance.position) >= 1:
                    instance.user_permissions.add(officer_permission)
                    instance.save()
                else:
                    instance.user_permissions.remove(officer_permission)
                    instance.save()

                messages.success(request, "Member updated successfully")
                return redirect('users:view_all')
        else: #Get Request
            form = FullMemberForm(instance=instance)

            context = {
                "form": form,
                "member_id": instance.id,
                'button_text': 'Update Member',
            }
            return render(request, 'users/edit.html', context)

    else:
        return HttpResponse("You don't have permission to change other users.", status=403)

@login_required()
@permission_required("users.officer", raise_exception=True)
def setAlumni(request, member_id):
    instance = get_object_or_404(Member, pk=member_id)

    instance.current_member = False
    if len(instance.position) >= 1:
        officer_permission = Permission.objects.get(codename='officer')
        instance.user_permissions.remove(officer_permission)
    instance.position = []
    instance.save()

    return redirect('users:view_all')



@login_required()
@permission_required("users.view_member", raise_exception=True)
def viewAll(request, sort_by='last_name'):
    members = Member.objects.filter(hidden=False, is_active=True)
    if request.user.has_perm('users.officer'):
        officer = True
    else:
        officer = False


    context = {
        "members": members,
        "sort_by": sort_by,
        "officer": officer,
    }

    return render(request, 'users/all.html', context)
