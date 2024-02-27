from django.urls import reverse
from django.shortcuts import redirect
from django.views.generic import TemplateView
import requests
from .utils import get_deezer_album_info


class HomePageView(TemplateView):
    """
    A view for rendering the home page.

    Attributes:
        template_name (str): The name of the template to render.
    """

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        """
        Get the context data for rendering the home page.

        Returns:
            dict: The context data.
        """

        context = super().get_context_data(**kwargs)

        api_url = 'http://127.0.0.1:7000/api/simple/'
        response = requests.get(api_url)

        if response.status_code == 200:
            api_data = response.json()

            formatted_data = [
                {'title': item['title'], 'artist': item['artist'], 'year': item['year']} for item in api_data]

            context['api_data'] = formatted_data

        else:
            context['error_message'] = 'Error obtaining data from the API'

        return context


class BaseRecordView(TemplateView):
    """
    A base view for rendering records.

    Attributes:
        template_name (str): The name of the template to render.
    """

    template_name = "records.html"

    def retrieve_album_info(self, deezer_id):
        """
        Retrieve additional album information from Deezer.

        Args:
            deezer_id (str): The Deezer ID of the album.

        Returns:
            dict: Additional information about the album.
        """

        return get_deezer_album_info(deezer_id)

    def get_context_data(self, **kwargs):
        """
        Get the context data for rendering records.

        Returns:
            dict: The context data.
        """

        context = super().get_context_data(**kwargs)

        url = 'http://127.0.0.1:7000/api/all/'
        token = '[token]'  # Replace with your token

        headers = {'Authorization': f'Token {token}'}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            api_data = response.json()

            for item in api_data:
                deezer_id = item['deezer_id']
                deezer_info = self.retrieve_album_info(deezer_id)
                item.update(deezer_info)

            formatted_data = [
                {'title': item['title'],
                 'artist': item['artist'],
                 'year': item['year'],
                 'genre': item['genre'],
                 'price': item['price'],
                 'available_units': item['available_units'],
                 'url': (reverse('record_detail', kwargs={'pk': item['id']})),
                 'fixed': 'fixed value',
                 'deezer_id': item['deezer_id'],
                 } for item in api_data]

            context['records'] = zip(api_data, formatted_data)
            context['api_data'] = api_data
            context['formatted_data'] = formatted_data

        else:
            context['error_message'] = 'Error obtaining data from the API'

        return context


class DetailRecordView(TemplateView):
    """
    A view for rendering the details of a record.

    Attributes:
        template_name (str): The name of the template to render.
    """

    template_name = 'record_details.html'

    def retrieve_album_info(self, deezer_id):
        """
        Retrieve additional album information from Deezer.

        Args:
            deezer_id (str): The Deezer ID of the album.

        Returns:
            dict: Additional information about the album.
        """

        return get_deezer_album_info(deezer_id)

    def get_context_data(self, **kwargs):
        """
        Get the context data for rendering record details.

        Returns:
            dict: The context data.
        """

        context = super().get_context_data(**kwargs)
        record_id = self.kwargs.get('pk')
        url = f'http://127.0.0.1:7000/api/{record_id}/'

        token = '[token]'  # Replace with your token
        headers = {'Authorization': f'Token {token}'}

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            record_data = response.json()
            context['record'] = record_data

            deezer_id = record_data.get('deezer_id')

            if deezer_id:
                deezer_info = self.retrieve_album_info(deezer_id)
                context['deezer_info'] = deezer_info
        else:
            context['error_message'] = 'Error obtaining data from the API'

        return context
