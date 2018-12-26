from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required, login_required
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from .models import Member
from .forms import MemberForm, FullMemberForm

# @permission_required('users.add', raise_exception=True)
@login_required()
def add(request):
    if request.user.has_perm('users.add_member'):
        if request.method == 'POST':
            pass
        else:
            form = FullMemberForm()
            return render(request, 'users/add.html', {"form": form})
    else:
        raise PermissionDenied("You don't have permission to add users.")




def remove(request):
    if request.user.has_perm(users.delete_member):
        if request.user.has_perm(users.change_other_member):
            if request.method == 'POST':
                pass
            else:
                return render(request, 'users/remove.html')
        else:
            raise PermissionDenied("You don't have permission to change users.")
    else:
        raise PermissionDenied("You don't have permission to delete users.")




def edit(request, member_id):
    if request.user.has_perm('users.change_member'):
        instance = get_object_or_404(Member, pk=member_id)

        if instance.username == request.user.username:
            print("MODIFYING OWN USER")
            # Modify own user

            if request.method == 'POST':
                form = MemberForm(request.POST, request.FILES, instance=instance)
                if form.is_valid():
                    instance = form.save()
                    # instance.save()
                    messages.success(request, "Member updated successfully")

                    next = request.POST.get('next', '/')
                    return redirect('users-view-all')
            else:
                form = MemberForm(instance=instance)

                context = {
                    "form": form,
                    "member_id": instance.id,
                    'button_text': 'Update Member',
                }
                return render(request, 'users/edit.html', context)

        elif request.user.has_perm('users.change_other_member'):
            print("MODIFYING OTHER USER")
            #TODO: Modify other user

            if request.method == 'POST':
                form = MemberForm(request.POST, request.FILES, instance=instance)
                if form.is_valid():
                    instance = form.save()
                    # instance.save()
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
    else:
        raise PermissionDenied("You don't have permission to change users.")







def view(request):
    pass

def viewAll(request, sort_by='last_name'):
    members = Member.objects.filter(hidden=False)


    context = {
        "members": members,
        "sort_by": sort_by,
    }

    return render(request, 'users/all.html', context)
