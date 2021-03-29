import pygal_maps_world.maps
import pygal

wm = pygal.maps.world.World()
wm.title = 'North, Centeral, and South America'

wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South AMerica', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 
        'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('americas.svg')

