import logging

from rest_framework.decorators import action
from rest_framework.exceptions import ParseError
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from xml.etree import ElementTree

from xml_converter.utils import element_tree_to_dict


logger = logging.getLogger(__name__)


class ConverterViewSet(ViewSet):
    parser_classes = [MultiPartParser]

    @action(methods=['POST'], detail=False, url_path='convert')
    def convert(self, request, **kwargs):

        try:
            xml_file = request.data['file']
        except KeyError as exc:
            error_message = 'Invalid request.'
            logger.exception(f'{error_message} {exc}')
            raise ParseError({'message': error_message})

        try:
            element_tree = ElementTree.parse(xml_file)
        except ElementTree.ParseError as exc:
            error_message = 'Invalid XML file.'
            logger.exception(f'{error_message} {exc}')
            return ParseError({'message': error_message})

        serialized_xml = element_tree_to_dict(element_tree.getroot())
        return Response(serialized_xml)
