import requests


# JSON Format
# {
#  "time": 32,
#  "energy": 0.5
# }
#
class Datasend:

    def __init__(self, url):
        self.__url = url

    def geturl(self):
        return self.__url

    def send(self, time, energy):
        reply = requests.post(url=self.geturl(), json = {"time": time, "energy": energy})
        print(reply.status_code)


# Class example
# ds = Datasend("https://i-ba-pren.flaviowaser.ch/upload-data.php")
# ds.send(1,2)