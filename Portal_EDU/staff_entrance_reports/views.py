from forms import StaffEntranceReportForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from .models import StaffEntranceReport

# Create your views here.

def create_staff_entrance_report(request):
    if request.POST:
        form = StaffEntranceReportForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/staff-entrance-reports')
    else:
        form = StaffEntranceReportForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_staff_entrance_report.html', args)

def view_all_staff_entrance_reports(request):
    template_name = "view_all_staff_entrance_reports.html"
    staffentrancereports = StaffEntranceReport.objects.all()
    return render_to_response(template_name, {'staffentrancereports':staffentrancereports})

def view_staff_entrance_report(request, pk):
    template_name = "view_staff_entrance_report.html"
    staffentrancereport = StaffEntranceReport.objects.get(pk=pk)
    return render_to_response(template_name, {'staffentrancereport':staffentrancereport})