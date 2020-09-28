from django.shortcuts import render
# -*- coding: utf-8 -*-
from .models import truck_header_report, truck_list_report,truck,truck_type,employee,master_package, dn_list_report, dn_header_report
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML

import math
import tempfile

def index(request):
    return render(request, 'blog/index.html', {})

def truck_control(request):
    return render(request, 'blog/truck_control.html', {})

def delivery_note(request):
    return render(request, 'blog/delivery_note.html', {})

def truck_control_pdf(request):
    page = 10

    all_count = truck_list_report.objects.count()
    all_page_no = math.ceil(all_count/page)

    """Generate pdf."""
    list_pdf = []
    for i in range(0, all_page_no):
        query_max = (i+1)*page
        if query_max > all_count:
            query_max = all_count
        header_report = truck_header_report.objects.filter(truck_control_no= '1234')
        list_report = truck_list_report.objects.all().order_by('list_no')[(i*page):query_max]
        html_string = render_to_string('blog/truck_control.html', {'header_report':header_report, 'list_report': list_report, 'start_index': (i*page), 'page_no': (i+1), 'all_page_no': all_page_no})
        pdf = HTML(string=html_string)
        list_pdf.append(pdf)
    
    lid_render = []
    val = []
    boo_first = True
    pdf_data = None

    for pdf in list_pdf:
        if boo_first:
            boo_first = False
            pdf_data = pdf.render()
        lid_render.append(pdf.render())

    for doc in lid_render:
        for p in doc.pages:
            val.append(p)

    pdf_file = pdf_data.copy(val).write_pdf() # use metadata of pdf_first

    http_response = HttpResponse(pdf_file, content_type='application/pdf')
    http_response['Content-Disposition'] = 'attachment; filename="truck_control.pdf"'

    return http_response

def index_pdf(request):
    """Generate pdf."""
    # Model data
    #entryreport = Entry.objects.all().order_by('rating')

    # Rendered
    html_string = render_to_string('blog/index.html')
    html = HTML(string=html_string)
    result = html.write_pdf()
    # Creating http response
    response = HttpResponse(content_type='application/pdf;')
    response['Content-Disposition'] = 'inline; filename=truck_control.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())

    return response

def delivery_note_pdf(request):
    page = 10

    all_count = dn_list_report.objects.count()
    all_page_no = math.ceil(all_count/page)

    """Generate pdf."""
    
    list_pdf = []
    for i in range(0, all_page_no):
        query_max = (i+1)*page
        if query_max > all_count:
            query_max = all_count
        header_report = dn_header_report.objects.filter(dn_no='KOCH200928001')
        list_report = dn_list_report.objects.all().order_by('list_no')[(i*page):query_max]
        html_string = render_to_string('blog/delivery_note.html', {'header_report': header_report, 'list_report': list_report, 'start_index': (i*page), 'page_no': (i+1), 'all_page_no': all_page_no})
        pdf = HTML(string=html_string)
        list_pdf.append(pdf)
    
    lid_render = []
    val = []
    boo_first = True
    pdf_data = None

    for pdf in list_pdf:
        if boo_first:
            boo_first = False
            pdf_data = pdf.render()
        lid_render.append(pdf.render())

    for doc in lid_render:
        for p in doc.pages:
            val.append(p)

    pdf_file = pdf_data.copy(val).write_pdf() # use metadata of pdf_first

    http_response = HttpResponse(pdf_file, content_type='application/pdf')
    http_response['Content-Disposition'] = 'attachment; filename="deliver_note_report.pdf"'

    return http_response

