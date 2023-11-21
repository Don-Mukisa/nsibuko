# Create your views here.
# requisitions/views.py

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Requisition
from .forms import RequisitionForm

@login_required
def requisition_detail(request, requisition_id):
    requisition = get_object_or_404(Requisition, id=requisition_id)
    form = RequisitionForm(instance=requisition)

    if request.user.is_staff:
        form.set_admin_permissions()

    if request.method == 'POST':
        form = RequisitionForm(request.POST, instance=requisition)
        if form.is_valid():
            form.save()

    return render(request, 'requisitions/requisition_detail.html', {'form': form, 'requisition': requisition})
