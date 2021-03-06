from lxml.etree import Element, SubElement, ElementTree

# Testprogram container
RavenRevA = Element('Testprogram', name='RavenRevA')

# Tests and Flows
RavenTests = SubElement(RavenRevA, 'TestRef', name='RavenTests')
Gpio18_PinCont = SubElement(RavenTests, 'TestFlow', name='Gpio18_PinCont')
Gpio18_Opens = SubElement(Gpio18_PinCont, 'Test', name='Gpio18_Opens',
                          testtype='BASIC', 
                          pinref='GpioPins', 
                          force='100e-6',
                          lolim='200e-3', 
                          hilim='1.5', 
                          delay='2e-3')
Gpio18_Shorts = SubElement(Gpio18_PinCont, 'Test', name='Gpio18_Shorts', 
                           testtype='BASIC',
                           pinref='JtagPins', 
                           force='100e-6',
                           lolim='200e-3', 
                           hilim='1.5',
                           delay='2e-3')


# Pins and Pingroups
RavenPins = SubElement(RavenRevA, 'PinRef', name='RavenPins')
# Gpio18_Opens_Pins = SubElement(RavenPins, 'PinGroup', name='Gpio18_Opens_Pins', pintype='IO')

GpioPins = SubElement(RavenPins, 'PinGroup', name='GpioPins', pintype='IO')
SubElement(GpioPins, 'Pin', name='PWROK')
SubElement(GpioPins, 'Pin', name='RST_L')

JtagPins = SubElement(RavenPins, 'PinGroup', name='JtagPins', pintype='IO')
SubElement(JtagPins, 'Pin', name='TCK')
SubElement(JtagPins, 'Pin', name='TMS')

Pins = SubElement(RavenPins, 'Pins', name='AllPins')
SubElement(Pins, 'Pin', name='PWROK', pintype='IO', channel = '0x0000')
SubElement(Pins, 'Pin', name='RST_L', pintype='IO', channel = '0x0001')
SubElement(Pins, 'Pin', name='TCK', pintype='IO', channel = '0x0002')
SubElement(Pins, 'Pin', name='TMS', pintype='IO', channel = '0x0003')

Testprogram = ElementTree(RavenRevA)
Testprogram.write('Testprogram.xml', pretty_print=True)

        