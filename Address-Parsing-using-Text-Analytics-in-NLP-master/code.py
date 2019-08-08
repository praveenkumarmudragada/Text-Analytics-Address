import requests
import json
from bs4 import BeautifulSoup

class GetZipInfo:
    """
    Using API, this class gives the city, state information
    from the zipcode provided
    """
    def construct_url(self, hostname, api_key, format, units, zipcode): #method to construct the url format
        """
        :param hostname:
        :param api_key:
        :param format:
        :param units:
        :param zipcode:
        :return:
        """
 
        url = hostname+api_key+'/'+'info.'+format+'/'+zipcode+'/'+units
        return url

    @staticmethod
    def get_api_key():
        response = requests.get('https://www.zipcodeapi.com/API#zipToLoc')  #sending HTTP request to the url
        html = response.text   #response stored in html
        soup = BeautifulSoup(html, 'html.parser')  #using bs4 did web srcaping to parse the api key 
        return (soup.find('input',{'name':'api_key'})['value'])  #finding the value of the api key

    def convert_json(self, response):
        """
        :param response:
        :return:
        """
        decoded_string = response.content.decode('utf8')  
        info = json.loads(decoded_string)
        return info

    def get_info_from_zip(self, zipcode):
        """
        :param zipcode:
        :return:
        """
        host = 'https://www.zipcodeapi.com/rest/'
        api_key = self.get_api_key()
        format = 'json'
        units = 'miles'
        url = self.construct_url(host, api_key, format, units, zipcode)
        response = requests.get(url)
        info = self.convert_json(response)
        return info


if __name__ == '__main__':
    """Driver code"""
    zipcode = input("Please enter the zipcode: ")
    zipobj = GetZipInfo()
    info = zipobj.get_info_from_zip(zipcode)
    print(info)