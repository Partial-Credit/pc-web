from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required, login_required
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from .models import Member
from .forms import MemberForm, FullMemberForm


@permission_required('users.add_member')
def add(request):
    if request.user.has_perm('users.add_member'):
        if request.method == 'POST':
            pass
        else:
            form = FullMemberForm()
            return render(request, 'users/add.html', {"form": form})
    else:
        raise PermissionDenied("You don't have permission to add users.")



@permission_required(['users.delete_member', 'users.change_other_member'])
def remove(request, member_id):
    instance = get_object_or_404(Member, pk=member_id)

    # Set is_active to False instead of deleting. This keeps the data around
    # so references to the user object such as arranger credit can be maintained.
    # The assumed use case for removing a user is if a member leaves the group
    # early before they graduate.
    instance.is_active = False

    instance.current_member = False
    instance.position = None
    instance.save()

    return redirect('users:view_all')





@permission_required('users.change_member')
def edit(request, member_id):
    instance = get_object_or_404(Member, pk=member_id)

    if instance.username == request.user.username:
        # User is modifying their own object

        if request.method == 'POST':
            form = MemberForm(request.POST, request.FILES, instance=instance)
            if form.is_valid():
                instance = form.save()
                # instance.save()
                messages.success(request, "Member updated successfully")

                next = request.POST.get('next', '/')
                return redirect('view_all')
        else:
            form = MemberForm(instance=instance)

            context = {
                "form": form,
                "member_id": instance.id,
                'button_text': 'Update Member',
            }
            return render(request, 'users/edit.html', context)

    # If user isn't trying to change their own object check if they have permission to modify others
    elif request.user.has_perm('users.change_other_member'):
        # Modify other user

        if request.method == 'POST':
            form = MemberForm(request.POST, request.FILES, instance=instance)
            if form.is_valid():
                instance = form.save()
                messages.success(request, "Member updated successfully")

                next = request.POST.get('next', '/')
                return redirect(next)
        else:
            form = MemberForm(instance=instance)

            context = {
                "form": form,
                "member_id": instance.id,
                'button_text': 'Update Member',
            }
            return render(request, 'users/edit.html', context)

    else:
        raise PermissionDenied("You don't have permission to change other users.")








def view(request):
    pass


@permission_required("users.view_member")
def viewAll(request, sort_by='last_name'):
    members = Member.objects.filter(hidden=False, is_active=True)
    if request.user.has_perm('users.change_other_member'):
        edit_other = True
    else:
        edit_other = False


    context = {
        "members": members,
        "sort_by": sort_by,
        "edit_other": edit_other,
    }

    return render(request, 'users/all.html', context)
