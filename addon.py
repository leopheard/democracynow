from xbmcswift2 import Plugin, xbmcgui
from resources.lib import democracynow

plugin = Plugin()
url1 = "https://www.democracynow.org/podcast-video.xml"
url1 = "https://www.democracynow.org/podcast-video.xml"
url3 = "https://www.democracynow.org/podcast.xml"
@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://assets.democracynow.org/assets/DN-Podcast-VIDEO-c7653c36fee413a3bc7447af1ebd42f39f27f1dfd49f2e60f389c3f31a70a448.jpg"},
        {
            'label': plugin.get_string(30002),
            'path': plugin.url_for('episodes2'),
            'thumbnail': "https://assets.democracynow.org/assets/DN-Podcast-AUDIO-1d5df65d8936dcfd1387274443b3e0713c5f15dd3fa400331229f4ab39b5c19e.jpg"},
        {
            'label': plugin.get_string(30003),
            'path': plugin.url_for('episodes3'),
            'thumbnail': "https://assets.democracynow.org/assets/DN-Podcast-AUDIO-1d5df65d8936dcfd1387274443b3e0713c5f15dd3fa400331229f4ab39b5c19e.jpg"},
    ]
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup1 = democracynow.get_soup1(url1)
    playable_DN1 = democracynow.get_playable_DN1(soup1)
    items = democracynow.compile_playable_DN1(playable_DN1)
    return items
@plugin.route('/episodes2/')
def episodes2():
    soup2 = democracynow.get_soup1(url2)
    playable_DN2 = democracynow.get_playable_DN2(soup2)
    items = democracynow.compile_playable_DN2(playable_DN2)
    return items
@plugin.route('/episodes3/')
def episodes3():
    soup3 = democracynow.get_soup3(url3)
    playable_DN3 = democracynow.get_playable_DN3(soup3)
    items = democracynow.compile_playable_DN3(playable_DN3)
    return items
if __name__ == '__main__':
    plugin.run()
