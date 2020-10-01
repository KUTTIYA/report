from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from io import BytesIO

from xhtml2pdf import pisa

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("utf-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        pdf = render_to_pdf('xhtml2pdfapp/pdf.html')
        return HttpResponse(pdf, content_type='application/pdf')