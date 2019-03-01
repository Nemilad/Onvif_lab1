from onvif import ONVIFCamera
from time import sleep

# Connect
camera = ONVIFCamera('192.168.15.42', 80, 'nikshaim', 'xtPez8oCfcKnJRHl', 'C:/Python27/wsdl/')

# Get Hostname
print 'Camera`s hostname: ' + str(camera.devicemgmt.GetHostname().Name)

# Create media service
media_service = camera.create_media_service()
print 'Created media service object'

# Get media profile
media_profile = media_service.GetProfiles()[0]
print 'Getting media profile'

# Get token
token = media_profile._token
print 'Getting token'

# Create ptz service
ptz = camera.create_ptz_service()
print 'Created ptz service'

# Get ptz configuration

#Get available PTZ services
request = ptz.create_type('GetServiceCapabilities')
Service_Capabilities = ptz.GetServiceCapabilities(request)
print 'PTZ service capabilities:'
print Service_Capabilities

#Get PTZ status
status = ptz.GetStatus({'ProfileToken':token})
print 'Pan position:', status.Position.PanTilt._x
print 'Tilt position:', status.Position.PanTilt._y
print 'Zoom position:', status.Position.Zoom._x

# Get PTZ configuration options for getting option ranges
request = ptz.create_type('GetConfigurationOptions')
request.ConfigurationToken = media_profile.PTZConfiguration._token
ptz_configuration_options = ptz.GetConfigurationOptions(request)

# Get range of pan and tilt
XMAX = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].XRange.Max
XMIN = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].XRange.Min
YMAX = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].YRange.Max
YMIN = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].YRange.Min
print 'Getting range of pan and tilt'

#Stop movement request
request_s = ptz.create_type('Stop')
request_s.ProfileToken = media_profile._token
request_s.PanTilt = True
request_s.Zoom = True
print 'Created stop movement request'

#Continuous move | up down left right
request_c = ptz.create_type('ContinuousMove')
request_c.ProfileToken = media_profile._token

#UP
request_c.Velocity.PanTilt._x = 0
request_c.Velocity.PanTilt._y = YMAX
ptz.ContinuousMove(request_c)
sleep(2)
ptz.Stop(request_s)
print 'Moved up: 2s, max speed'

sleep(6)

# DOWN
request_c.Velocity.PanTilt._x = 0
request_c.Velocity.PanTilt._y = YMIN
ptz.ContinuousMove(request_c)
sleep(2)
ptz.Stop(request_s)
print 'Moved down: 2s, max speed'

sleep(6)

#LEFT
request_c.Velocity.PanTilt._x = XMIN
request_c.Velocity.PanTilt._y = 0
ptz.ContinuousMove(request_c)
sleep(2)
ptz.Stop(request_s)
print 'Moved left: 2s, max speed'

sleep(6)

#RIGHT
request_c.Velocity.PanTilt._x = XMAX
request_c.Velocity.PanTilt._y = 0
ptz.ContinuousMove(request_c)
sleep(2)
ptz.Stop(request_s)
print 'Moved right: 2s, max speed'

sleep(6)

#Absolute move
request_a = ptz.create_type('AbsoluteMove')
request_a.ProfileToken = media_profile._token

#Move to 0,0
request_a.Speed.PanTilt._x = 1
request_a.Speed.PanTilt._y = 1
request_a.Position.PanTilt._x = 0
request_a.Position.PanTilt._y = 0
request_a.Position.Zoom._x = 0
ptz.AbsoluteMove(request_a)
print 'moving to 0,0'

sleep(12)

status = ptz.GetStatus({'ProfileToken':token})
print 'Pan position:', status.Position.PanTilt._x
print 'Tilt position:', status.Position.PanTilt._y
print 'Zoom position:', status.Position.Zoom._x

#Move to 0.3,0
request_a.Speed.PanTilt._x = 1
request_a.Speed.PanTilt._y = 1
request_a.Position.PanTilt._x = 0.3
request_a.Position.PanTilt._y = 0
request_a.Position.Zoom._x = 0
ptz.AbsoluteMove(request_a)
print 'moving to 0.3,0'

sleep(12)

status = ptz.GetStatus({'ProfileToken':token})
print 'Pan position:', status.Position.PanTilt._x
print 'Tilt position:', status.Position.PanTilt._y
print 'Zoom position:', status.Position.Zoom._x

#Move to 0.3,0.3
request_a.Speed.PanTilt._x = 1
request_a.Speed.PanTilt._y = 1
request_a.Position.PanTilt._x = 0.3
request_a.Position.PanTilt._y = 0.3
request_a.Position.Zoom._x = 0
ptz.AbsoluteMove(request_a)
print 'moving to 0.3,0.3'

sleep(12)

status = ptz.GetStatus({'ProfileToken':token})
print 'Pan position:', status.Position.PanTilt._x
print 'Tilt position:', status.Position.PanTilt._y
print 'Zoom position:', status.Position.Zoom._x

#Move to 0,0
request_a.Speed.PanTilt._x = 1
request_a.Speed.PanTilt._y = 1
request_a.Position.PanTilt._x = 0
request_a.Position.PanTilt._y = 0
request_a.Position.Zoom._x = 0
ptz.AbsoluteMove(request_a)
print 'moving to 0,0'

sleep(12)

status = ptz.GetStatus({'ProfileToken':token})
print 'Pan position:', status.Position.PanTilt._x
print 'Tilt position:', status.Position.PanTilt._y
print 'Zoom position:', status.Position.Zoom._x

sleep(5)

#Zoom

request_a.Position.PanTilt._x = 0
request_a.Position.PanTilt._y = 0
request_a.Position.Zoom._x = 1
ptz.AbsoluteMove(request_a)
print 'zoom to 1'

sleep(10)

request_a.Position.PanTilt._x = 0
request_a.Position.PanTilt._y = 0
request_a.Position.Zoom._x = 0
ptz.AbsoluteMove(request_a)
print 'zoom to 0'

sleep(10)

