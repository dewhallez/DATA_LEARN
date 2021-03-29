import pygal_maps_world.maps
import pygal

wm = pygal.maps.world.World()
wm.title = 'Populations of Countries in north America'
wm.add('North America', { 'ca': 48126000, 'us': 50934000, 'mx': 153423000})

wm.render_to_file('na.populations.svg')