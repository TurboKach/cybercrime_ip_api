import time
from ipaddress import ip_address, ip_network

from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view

import db.views


def is_in_network(ip: str, network: str) -> bool:
    return ip_address(ip) in ip_network(network)


@csrf_exempt
@api_view(['GET'])
def get_ips(request) -> JsonResponse:
    """
    :return: Список всех IP и подсетей, удовлетворяющих условиям
    """
    try:
        time_from = request.GET.get('time_from')
        time_to = request.GET.get('time_to')
        ip_list = request.GET.get('list')

        response = []  # TODO забрать данные из БД

        return JsonResponse(response, status=status.HTTP_200_OK)

    except Exception as e:
        response = {
            'status': {
                'error': e.__class__.__name__,
                'args': e.args
            },
        }
        return JsonResponse(response, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET'])
def get_lists(request) -> JsonResponse:
    """
    На вход IP (обязательно) и время (необязательно), на выходе все списки.
    (Обратите внимание на п.5.а, эта функция должна быть задействована.)
    :return: Списки, которым принадлежит IP
    """
    try:
        ip = request.GET.get('ip')
        time_to = request.GET.get('time_to')

        response = []  # TODO забрать данные из БД

        return JsonResponse(response, status=status.HTTP_200_OK)

    except Exception as e:
        response = {
            'status': {
                'error': e.__class__.__name__,
                'args': e.args
            },
        }
        return JsonResponse(response, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET'])
def update_lists(request) -> JsonResponse:
    db.views.update_ipsets()
    response = 'IP lists update initialized. It may take a few minutes to update.'
    return JsonResponse(response, status=status.HTTP_202_ACCEPTED)
