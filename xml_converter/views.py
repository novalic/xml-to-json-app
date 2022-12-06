import logging

from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.status import HTTP_400_BAD_REQUEST
from xml.etree import ElementTree

from xml_converter.utils import element_tree_to_dict


logger = logging.getLogger(__name__)


def upload_page(request):
    if request.method == 'POST':
        try:
            xml_file = request.FILES['file']
        except KeyError as exc:
            error_message = 'Invalid request.'
            logger.exception(f'{error_message} {exc}')
            return JsonResponse({'message': error_message}, status=HTTP_400_BAD_REQUEST)

        try:
            element_tree = ElementTree.parse(xml_file)
        except ElementTree.ParseError as exc:
            error_message = 'Invalid XML file.'
            logger.exception(f'{error_message} {exc}')
            return JsonResponse({'message': error_message}, status=HTTP_400_BAD_REQUEST)

        serialized_xml = element_tree_to_dict(element_tree.getroot())
        return JsonResponse(serialized_xml)

    return render(request, 'upload_page.html')
