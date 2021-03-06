from skidl import SKIDL, TEMPLATE, Part, Pin, SchLib

SKIDL_lib_version = '0.0.1'

motor_drivers = SchLib(tool=SKIDL).add_parts(*[
        Part(name='A4950E',dest=TEMPLATE,tool=SKIDL,keywords='full-bridge h-bridge',description='Full-Bridge, DMOS PWM, Motor Driver, 40V, 3.5A, -40 to +125C',ref_prefix='U',num_units=1,fplist=['SOIC-*1EP*'],do_erc=True,aliases=['A4950K'],pins=[
            Pin(num='1',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='2',name='IN2',do_erc=True),
            Pin(num='3',name='IN1',do_erc=True),
            Pin(num='4',name='VREF',func=Pin.PASSIVE,do_erc=True),
            Pin(num='5',name='VBB',func=Pin.PWRIN,do_erc=True),
            Pin(num='6',name='OUT1',func=Pin.PWROUT,do_erc=True),
            Pin(num='7',name='LSS',func=Pin.PWRIN,do_erc=True),
            Pin(num='8',name='OUT2',func=Pin.PWROUT,do_erc=True),
            Pin(num='9',name='PAD',func=Pin.PWRIN,do_erc=True)]),
        Part(name='DRV8308',dest=TEMPLATE,tool=SKIDL,keywords='bldc mosfet-driver hall-sensor',description='Brushless DC motor controller, closed loop, hall sensor inputs, current limiting, SPI interface',ref_prefix='U',num_units=1,fplist=['QFN*1EP*6x6mm*Pitch0.5mm*'],do_erc=True,pins=[
            Pin(num='1',name='UHP',do_erc=True),
            Pin(num='2',name='UHN',do_erc=True),
            Pin(num='3',name='VHP',do_erc=True),
            Pin(num='4',name='VHN',do_erc=True),
            Pin(num='5',name='WHP',do_erc=True),
            Pin(num='6',name='WHN',do_erc=True),
            Pin(num='7',name='VSW',func=Pin.PWROUT,do_erc=True),
            Pin(num='8',name='FGFB',func=Pin.OUTPUT,do_erc=True),
            Pin(num='9',name='FGINN_TACH',do_erc=True),
            Pin(num='10',name='FGINP',func=Pin.BIDIR,do_erc=True),
            Pin(num='20',name='BRAKE',do_erc=True),
            Pin(num='30',name='CP1',func=Pin.PASSIVE,do_erc=True),
            Pin(num='40',name='WLSG',func=Pin.OUTPUT,do_erc=True),
            Pin(num='11',name='SCLK',do_erc=True),
            Pin(num='21',name='DIR',do_erc=True),
            Pin(num='31',name='ISEN',do_erc=True),
            Pin(num='41',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='12',name='SCS',do_erc=True),
            Pin(num='22',name='ENABLE',do_erc=True),
            Pin(num='32',name='UHSG',func=Pin.OUTPUT,do_erc=True),
            Pin(num='13',name='SMODE',do_erc=True),
            Pin(num='23',name='RESET',do_erc=True),
            Pin(num='33',name='U',do_erc=True),
            Pin(num='14',name='SDATAI',do_erc=True),
            Pin(num='24',name='VREG',func=Pin.PWROUT,do_erc=True),
            Pin(num='34',name='ULSG',func=Pin.OUTPUT,do_erc=True),
            Pin(num='15',name='SDATAO',func=Pin.OUTPUT,do_erc=True),
            Pin(num='25',name='VINT',func=Pin.PASSIVE,do_erc=True),
            Pin(num='35',name='VHSG',func=Pin.OUTPUT,do_erc=True),
            Pin(num='16',name='FGOUT',func=Pin.OUTPUT,do_erc=True),
            Pin(num='26',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='36',name='V',do_erc=True),
            Pin(num='17',name='~FAULTn',func=Pin.OUTPUT,do_erc=True),
            Pin(num='27',name='VM',func=Pin.PWRIN,do_erc=True),
            Pin(num='37',name='VLSG',func=Pin.OUTPUT,do_erc=True),
            Pin(num='18',name='~LOCKn',func=Pin.OUTPUT,do_erc=True),
            Pin(num='28',name='VCP',func=Pin.PASSIVE,do_erc=True),
            Pin(num='38',name='WHSG',func=Pin.OUTPUT,do_erc=True),
            Pin(num='19',name='CLKIN',do_erc=True),
            Pin(num='29',name='CP2',func=Pin.PASSIVE,do_erc=True),
            Pin(num='39',name='W',do_erc=True)]),
        Part(name='DRV8711',dest=TEMPLATE,tool=SKIDL,keywords='Stepper driver',description='Stepper motor controller, external N-channel MOSFET, single bipolar stepper motor, dual brushed DC motors',ref_prefix='U',num_units=1,fplist=['HTSSOP-38'],do_erc=True,pins=[
            Pin(num='1',name='CP1',func=Pin.BIDIR,do_erc=True),
            Pin(num='2',name='CP2',func=Pin.BIDIR,do_erc=True),
            Pin(num='3',name='VCP',func=Pin.BIDIR,do_erc=True),
            Pin(num='4',name='VM',func=Pin.PWRIN,do_erc=True),
            Pin(num='5',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='6',name='V5',func=Pin.PWROUT,do_erc=True),
            Pin(num='7',name='VINT',func=Pin.PWRIN,do_erc=True),
            Pin(num='8',name='SLEEPn',do_erc=True),
            Pin(num='9',name='RESET',do_erc=True),
            Pin(num='10',name='STEP/AIN1',do_erc=True),
            Pin(num='20',name='BEMF',func=Pin.OUTPUT,do_erc=True),
            Pin(num='30',name='AOUT2',func=Pin.OUTPUT,do_erc=True),
            Pin(num='11',name='DIR/AIN2',do_erc=True),
            Pin(num='21',name='BOUT2',func=Pin.OUTPUT,do_erc=True),
            Pin(num='31',name='A2HS',func=Pin.OUTPUT,do_erc=True),
            Pin(num='12',name='BIN1',do_erc=True),
            Pin(num='22',name='B2HS',func=Pin.OUTPUT,do_erc=True),
            Pin(num='32',name='A2LS',func=Pin.OUTPUT,do_erc=True),
            Pin(num='13',name='BIN2',do_erc=True),
            Pin(num='23',name='B2LS',func=Pin.OUTPUT,do_erc=True),
            Pin(num='33',name='AISENN',do_erc=True),
            Pin(num='14',name='SCLK',do_erc=True),
            Pin(num='24',name='BISENN',do_erc=True),
            Pin(num='34',name='AISENP',do_erc=True),
            Pin(num='15',name='SDATI',do_erc=True),
            Pin(num='25',name='BISENP',do_erc=True),
            Pin(num='35',name='A1LS',func=Pin.OUTPUT,do_erc=True),
            Pin(num='16',name='SCS',do_erc=True),
            Pin(num='26',name='B1LS',func=Pin.OUTPUT,do_erc=True),
            Pin(num='36',name='A1HS',func=Pin.OUTPUT,do_erc=True),
            Pin(num='17',name='SDATO',func=Pin.OUTPUT,do_erc=True),
            Pin(num='27',name='B1HS',func=Pin.OUTPUT,do_erc=True),
            Pin(num='37',name='AOUT1',func=Pin.OUTPUT,do_erc=True),
            Pin(num='18',name='FAULTn',func=Pin.OUTPUT,do_erc=True),
            Pin(num='28',name='BOUT1',func=Pin.OUTPUT,do_erc=True),
            Pin(num='38',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='19',name='STALLn/BEMFVn',func=Pin.OUTPUT,do_erc=True),
            Pin(num='29',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='39',name='GND',func=Pin.PWRIN,do_erc=True)]),
        Part(name='L293',dest=TEMPLATE,tool=SKIDL,keywords='Half-H Driver Motor',description='Quadruple Half-H Drivers',ref_prefix='U',num_units=1,fplist=['DIP*W7.62mm*'],do_erc=True,aliases=['L293D'],pins=[
            Pin(num='1',name='EN1,2',do_erc=True),
            Pin(num='2',name='1A',do_erc=True),
            Pin(num='3',name='1Y',func=Pin.OUTPUT,do_erc=True),
            Pin(num='4',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='5',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='6',name='2Y',func=Pin.OUTPUT,do_erc=True),
            Pin(num='7',name='2A',do_erc=True),
            Pin(num='8',name='VCC2',func=Pin.PWRIN,do_erc=True),
            Pin(num='9',name='EN3,4',do_erc=True),
            Pin(num='10',name='3A',do_erc=True),
            Pin(num='11',name='3A',func=Pin.OUTPUT,do_erc=True),
            Pin(num='12',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='13',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='14',name='4Y',func=Pin.OUTPUT,do_erc=True),
            Pin(num='15',name='4A',do_erc=True),
            Pin(num='16',name='VCC1',func=Pin.PWRIN,do_erc=True)]),
        Part(name='L298(H)N',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='L298P',dest=TEMPLATE,tool=SKIDL,keywords='H-bridge motor driver',description='Dual full bridge motor driver, up to 46V, 4A',ref_prefix='U',num_units=1,do_erc=True,pins=[
            Pin(num='1',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='2',name='SENSE_A',func=Pin.PWRIN,do_erc=True),
            Pin(num='3',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='4',name='OUT1',func=Pin.OUTPUT,do_erc=True),
            Pin(num='5',name='OUT2',func=Pin.OUTPUT,do_erc=True),
            Pin(num='6',name='Vs',func=Pin.PWRIN,do_erc=True),
            Pin(num='7',name='IN1',do_erc=True),
            Pin(num='8',name='EnA',do_erc=True),
            Pin(num='9',name='IN2',do_erc=True),
            Pin(num='10',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='20',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='11',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='12',name='Vss',func=Pin.PWRIN,do_erc=True),
            Pin(num='13',name='IN3',do_erc=True),
            Pin(num='14',name='EnB',do_erc=True),
            Pin(num='15',name='IN4',do_erc=True),
            Pin(num='16',name='OUT3',func=Pin.OUTPUT,do_erc=True),
            Pin(num='17',name='OUT4',func=Pin.OUTPUT,do_erc=True),
            Pin(num='18',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='19',name='SENSE_B',func=Pin.PWRIN,do_erc=True)]),
        Part(name='PG001M',dest=TEMPLATE,tool=SKIDL,keywords='Support IC for SLA7042M/SLA7044M',description='Parallel to serial data converter for SLA7042M/SLA7044M',ref_prefix='U',num_units=1,fplist=['DIP*', 'PDIP*'],do_erc=True,pins=[
            Pin(num='1',name='~RESET~',do_erc=True),
            Pin(num='2',name='CLK_IN',do_erc=True),
            Pin(num='3',name='~CW~',do_erc=True),
            Pin(num='6',name='MSEL_1',do_erc=True),
            Pin(num='7',name='MSEL_2',do_erc=True),
            Pin(num='8',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='9',name='~MONITOR~',do_erc=True),
            Pin(num='10',name='DATA_B',func=Pin.OUTPUT,do_erc=True),
            Pin(num='11',name='DATA_A',func=Pin.OUTPUT,do_erc=True),
            Pin(num='13',name='~STROBE~',func=Pin.OUTPUT,do_erc=True),
            Pin(num='14',name='CLK_OUT',func=Pin.OUTPUT,do_erc=True),
            Pin(num='15',name='VECTOR',do_erc=True),
            Pin(num='16',name='Vdd',func=Pin.PWRIN,do_erc=True)]),
        Part(name='SLA7044M',dest=TEMPLATE,tool=SKIDL,keywords='Stepper driver',description='Unipolar PWM high-current motor driver',ref_prefix='U',num_units=2,fplist=['SLA704XM'],do_erc=True,aliases=['SLA7042M'],pins=[
            Pin(num='1',name='OUT',func=Pin.OUTPUT,do_erc=True),
            Pin(num='2',name='~STROBE~',do_erc=True),
            Pin(num='3',name='REF',do_erc=True),
            Pin(num='4',name='Vdd',func=Pin.PWRIN,do_erc=True),
            Pin(num='5',name='~CLOCK~',do_erc=True),
            Pin(num='6',name='DATA',do_erc=True),
            Pin(num='7',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='8',name='~OUT~',func=Pin.OUTPUT,do_erc=True),
            Pin(num='9',name='RS',do_erc=True),
            Pin(num='10',name='RS',do_erc=True),
            Pin(num='11',name='OUT',func=Pin.OUTPUT,do_erc=True),
            Pin(num='12',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='13',name='~STROBE~',do_erc=True),
            Pin(num='14',name='REF',do_erc=True),
            Pin(num='15',name='Vdd',func=Pin.PWRIN,do_erc=True),
            Pin(num='16',name='~CLOCK~',do_erc=True),
            Pin(num='17',name='DATA',do_erc=True),
            Pin(num='18',name='~OUT~',func=Pin.OUTPUT,do_erc=True)]),
        Part(name='SLA7070MPRT',dest=TEMPLATE,tool=SKIDL,keywords='Stepper driver',description='Unipolar 2-phase stepper motor driver, Full and Half step, 3A',ref_prefix='U',num_units=1,fplist=['ZIP23'],do_erc=True,aliases=['SLA7071MPRT', 'SLA7072MPRT', 'SLA7073MPRT'],pins=[
            Pin(num='1',name='OUTA',func=Pin.OUTPUT,do_erc=True),
            Pin(num='2',name='OUTA',func=Pin.OUTPUT,do_erc=True),
            Pin(num='3',name='~OUTA~',func=Pin.OUTPUT,do_erc=True),
            Pin(num='4',name='~OUTA~',func=Pin.OUTPUT,do_erc=True),
            Pin(num='5',name='SENSE_A',func=Pin.OUTPUT,do_erc=True),
            Pin(num='6',name='N.C.',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='7',name='M1',do_erc=True),
            Pin(num='8',name='M2',do_erc=True),
            Pin(num='9',name='M3',do_erc=True),
            Pin(num='10',name='CLOCK',do_erc=True),
            Pin(num='20',name='~OUTB~',func=Pin.OUTPUT,do_erc=True),
            Pin(num='11',name='VBB',func=Pin.PWRIN,do_erc=True),
            Pin(num='21',name='~OUTB~',func=Pin.OUTPUT,do_erc=True),
            Pin(num='12',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='22',name='OUTB',func=Pin.OUTPUT,do_erc=True),
            Pin(num='13',name='REF/SLEEP1',do_erc=True),
            Pin(num='23',name='OUTB',func=Pin.OUTPUT,do_erc=True),
            Pin(num='14',name='VDD',func=Pin.PWRIN,do_erc=True),
            Pin(num='15',name='RESET',do_erc=True),
            Pin(num='16',name='CW/CCW',do_erc=True),
            Pin(num='17',name='SYNC',do_erc=True),
            Pin(num='18',name='FLAG',func=Pin.OUTPUT,do_erc=True),
            Pin(num='19',name='SENSE_B',func=Pin.OUTPUT,do_erc=True)]),
        Part(name='SLA7075MPRT',dest=TEMPLATE,tool=SKIDL,keywords='Stepper driver',description='Unipolar 2-phase stepper motor driver, Microstep, 3A',ref_prefix='U',num_units=1,fplist=['ZIP23'],do_erc=True,aliases=['SLA7076MPRT', 'SLA7077MPRT', 'SLA7078MPRT'],pins=[
            Pin(num='1',name='OUTA',func=Pin.OUTPUT,do_erc=True),
            Pin(num='2',name='OUTA',func=Pin.OUTPUT,do_erc=True),
            Pin(num='3',name='~OUTA~',func=Pin.OUTPUT,do_erc=True),
            Pin(num='4',name='~OUTA~',func=Pin.OUTPUT,do_erc=True),
            Pin(num='5',name='SENSE_A',func=Pin.OUTPUT,do_erc=True),
            Pin(num='6',name='MO',func=Pin.OUTPUT,do_erc=True),
            Pin(num='7',name='M1',do_erc=True),
            Pin(num='8',name='M2',do_erc=True),
            Pin(num='9',name='M3',do_erc=True),
            Pin(num='10',name='CLOCK',do_erc=True),
            Pin(num='20',name='~OUTB~',func=Pin.OUTPUT,do_erc=True),
            Pin(num='11',name='VBB',func=Pin.PWRIN,do_erc=True),
            Pin(num='21',name='~OUTB~',func=Pin.OUTPUT,do_erc=True),
            Pin(num='12',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='22',name='OUTB',func=Pin.OUTPUT,do_erc=True),
            Pin(num='13',name='REF/SLEEP1',do_erc=True),
            Pin(num='23',name='OUTB',func=Pin.OUTPUT,do_erc=True),
            Pin(num='14',name='VDD',func=Pin.PWRIN,do_erc=True),
            Pin(num='15',name='RESET',do_erc=True),
            Pin(num='16',name='CW/CCW',do_erc=True),
            Pin(num='17',name='SYNC',do_erc=True),
            Pin(num='18',name='FLAG',func=Pin.OUTPUT,do_erc=True),
            Pin(num='19',name='SENSE_B',func=Pin.OUTPUT,do_erc=True)]),
        Part(name='STK672-040-E',dest=TEMPLATE,tool=SKIDL,keywords='Stepper driver',description='Stepper motor driver with microstepping controller, 1.5A',ref_prefix='U',num_units=1,fplist=['STK672-040-E'],do_erc=True,pins=[
            Pin(num='1',name='~B~',func=Pin.OUTPUT,do_erc=True),
            Pin(num='2',name='B',func=Pin.OUTPUT,do_erc=True),
            Pin(num='3',name='PG',func=Pin.PWRIN,do_erc=True),
            Pin(num='4',name='PG',func=Pin.PWRIN,do_erc=True),
            Pin(num='5',name='~A~',func=Pin.OUTPUT,do_erc=True),
            Pin(num='6',name='A',func=Pin.OUTPUT,do_erc=True),
            Pin(num='7',name='VCC',func=Pin.PWRIN,do_erc=True),
            Pin(num='8',name='Vref',do_erc=True),
            Pin(num='9',name='M1',do_erc=True),
            Pin(num='10',name='M2',do_erc=True),
            Pin(num='20',name='MO1',func=Pin.OUTPUT,do_erc=True),
            Pin(num='11',name='M3',do_erc=True),
            Pin(num='21',name='MO2',func=Pin.OUTPUT,do_erc=True),
            Pin(num='12',name='M4',do_erc=True),
            Pin(num='22',name='SG',func=Pin.PWRIN,do_erc=True),
            Pin(num='13',name='M5',do_erc=True),
            Pin(num='14',name='CLK',do_erc=True),
            Pin(num='15',name='CWB',do_erc=True),
            Pin(num='16',name='~RESET~',do_erc=True),
            Pin(num='17',name='RETURN',do_erc=True),
            Pin(num='18',name='ENABLE',do_erc=True),
            Pin(num='19',name='MOI',func=Pin.OUTPUT,do_erc=True)]),
        Part(name='STK672-080-E',dest=TEMPLATE,tool=SKIDL,keywords='Stepper driver',description='Stepper motor driver with microstepping controller, 2.8A',ref_prefix='U',num_units=1,fplist=['STK672-080-E'],do_erc=True,pins=[
            Pin(num='1',name='PG',func=Pin.PWRIN,do_erc=True),
            Pin(num='2',name='BB',func=Pin.OUTPUT,do_erc=True),
            Pin(num='3',name='B',func=Pin.OUTPUT,do_erc=True),
            Pin(num='4',name='AB',func=Pin.OUTPUT,do_erc=True),
            Pin(num='5',name='A',func=Pin.OUTPUT,do_erc=True),
            Pin(num='6',name='VCC',func=Pin.PWRIN,do_erc=True),
            Pin(num='7',name='Vref',do_erc=True),
            Pin(num='8',name='M1',do_erc=True),
            Pin(num='9',name='M2',do_erc=True),
            Pin(num='10',name='CWB',do_erc=True),
            Pin(num='11',name='CLOCK',do_erc=True),
            Pin(num='12',name='M3',do_erc=True),
            Pin(num='13',name='~RESET~',do_erc=True),
            Pin(num='14',name='MOI',func=Pin.OUTPUT,do_erc=True),
            Pin(num='15',name='ENABLE',do_erc=True)]),
        Part(name='STSPIN220',dest=TEMPLATE,tool=SKIDL,keywords='motor driver stepper',description='Low voltage stepper motor driver, 1.8V to 10V input, 1.3Arms output, 0.4Ω Rdson per phase (typical), QFN-16 package',ref_prefix='U',num_units=1,fplist=['QFN*3x3mm*Pitch0.5mm*'],do_erc=True,pins=[
            Pin(num='1',name='DIR',do_erc=True),
            Pin(num='2',name='STCK',do_erc=True),
            Pin(num='3',name='OUTA1',func=Pin.PWROUT,do_erc=True),
            Pin(num='4',name='SENSEA',func=Pin.PWROUT,do_erc=True),
            Pin(num='5',name='OUTA2',func=Pin.PWROUT,do_erc=True),
            Pin(num='6',name='VS',func=Pin.PWRIN,do_erc=True),
            Pin(num='7',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='8',name='OUTB2',func=Pin.PWROUT,do_erc=True),
            Pin(num='9',name='SENSEB',func=Pin.PWROUT,do_erc=True),
            Pin(num='10',name='OUTB1',func=Pin.PWROUT,do_erc=True),
            Pin(num='11',name='REF',do_erc=True),
            Pin(num='12',name='TOFF',do_erc=True),
            Pin(num='13',name='EN/FLT',func=Pin.BIDIR,do_erc=True),
            Pin(num='14',name='STBY/RESET',do_erc=True),
            Pin(num='15',name='MODE2',do_erc=True),
            Pin(num='16',name='MODE1',do_erc=True),
            Pin(num='17',name='EPAD',func=Pin.PWRIN,do_erc=True)]),
        Part(name='STSPIN230',dest=TEMPLATE,tool=SKIDL,keywords='motor driver half-bridge',description='Low voltage triple half-bridge motor driver, 1.8V to 10V input, 1.3Arms output, 0.4Ω Rdson per phase (typical), QFN-16 package',ref_prefix='U',num_units=1,fplist=['QFN*3x3mm*Pitch0.5mm*'],do_erc=True,pins=[
            Pin(num='1',name='INUH',do_erc=True),
            Pin(num='2',name='INUL',do_erc=True),
            Pin(num='3',name='OUTU',func=Pin.PWROUT,do_erc=True),
            Pin(num='4',name='SENSE',do_erc=True),
            Pin(num='5',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='6',name='VS',func=Pin.PWRIN,do_erc=True),
            Pin(num='7',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='8',name='OUTV',func=Pin.PWROUT,do_erc=True),
            Pin(num='9',name='SENSE',do_erc=True),
            Pin(num='10',name='OUTW',func=Pin.PWROUT,do_erc=True),
            Pin(num='11',name='INWL',do_erc=True),
            Pin(num='12',name='INWH',do_erc=True),
            Pin(num='13',name='EN/FLT',func=Pin.BIDIR,do_erc=True),
            Pin(num='14',name='STBY',do_erc=True),
            Pin(num='15',name='INVL',do_erc=True),
            Pin(num='16',name='INVH',do_erc=True),
            Pin(num='17',name='PAD',func=Pin.PWRIN,do_erc=True)]),
        Part(name='STSPIN240',dest=TEMPLATE,tool=SKIDL,keywords='motor driver dc brushed',description='Low voltage dual brush DC motor driver, 1.8V to 10V input, 1.3Arms output, 0.4Ω Rdson per phase (typical), QFN-16 package',ref_prefix='U',num_units=1,fplist=['QFN*3x3mm*Pitch0.5mm*'],do_erc=True,pins=[
            Pin(num='1',name='PHA',do_erc=True),
            Pin(num='2',name='PWMA',do_erc=True),
            Pin(num='3',name='OUTA1',func=Pin.PWROUT,do_erc=True),
            Pin(num='4',name='SENSEA',func=Pin.PWROUT,do_erc=True),
            Pin(num='5',name='OUTA2',func=Pin.PWROUT,do_erc=True),
            Pin(num='6',name='VS',func=Pin.PWRIN,do_erc=True),
            Pin(num='7',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='8',name='OUTB2',func=Pin.PWROUT,do_erc=True),
            Pin(num='9',name='SENSEB',func=Pin.PWROUT,do_erc=True),
            Pin(num='10',name='OUTB1',func=Pin.PWROUT,do_erc=True),
            Pin(num='11',name='REF',do_erc=True),
            Pin(num='12',name='TOFF',do_erc=True),
            Pin(num='13',name='EN/FLT',func=Pin.BIDIR,do_erc=True),
            Pin(num='14',name='STBY/RESET',do_erc=True),
            Pin(num='15',name='PHB',do_erc=True),
            Pin(num='16',name='PWMB',do_erc=True),
            Pin(num='17',name='EPAD',func=Pin.PWRIN,do_erc=True)]),
        Part(name='TMC262',dest=TEMPLATE,tool=SKIDL,keywords='trinamic tlc262 stepper',description='Driver for two-phase stepper motors with external mosfet',ref_prefix='U',num_units=1,fplist=['QFN*1EP*5x5mm*Pitch0.5mm*'],do_erc=True,pins=[
            Pin(num='1',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='2',name='HA1',func=Pin.OUTPUT,do_erc=True),
            Pin(num='3',name='HA2',func=Pin.OUTPUT,do_erc=True),
            Pin(num='4',name='BMA2',do_erc=True),
            Pin(num='5',name='BMA1',do_erc=True),
            Pin(num='6',name='LA1',func=Pin.OUTPUT,do_erc=True),
            Pin(num='7',name='LA2',func=Pin.OUTPUT,do_erc=True),
            Pin(num='8',name='SRA',do_erc=True),
            Pin(num='9',name='5VOUT',func=Pin.PWROUT,do_erc=True),
            Pin(num='10',name='SD0',func=Pin.TRISTATE,do_erc=True),
            Pin(num='20',name='BMB1',do_erc=True),
            Pin(num='30',name='DIR',do_erc=True),
            Pin(num='11',name='SDI',do_erc=True),
            Pin(num='21',name='BMB2',do_erc=True),
            Pin(num='31',name='STEP',do_erc=True),
            Pin(num='12',name='SCK',do_erc=True),
            Pin(num='22',name='HB2',func=Pin.OUTPUT,do_erc=True),
            Pin(num='32',name='TST_MODE',do_erc=True),
            Pin(num='13',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='23',name='HB1',func=Pin.OUTPUT,do_erc=True),
            Pin(num='33',name='DIE_PAD',do_erc=True),
            Pin(num='14',name='CSN',do_erc=True),
            Pin(num='24',name='VHS',func=Pin.PWRIN,do_erc=True),
            Pin(num='15',name='~ENN~',do_erc=True),
            Pin(num='25',name='VS',func=Pin.PWRIN,do_erc=True),
            Pin(num='16',name='CLK',do_erc=True),
            Pin(num='26',name='TST_ANA',func=Pin.OUTPUT,do_erc=True),
            Pin(num='17',name='SRB',do_erc=True),
            Pin(num='27',name='SG_TST',func=Pin.OUTPUT,do_erc=True),
            Pin(num='18',name='LB2',func=Pin.OUTPUT,do_erc=True),
            Pin(num='28',name='GNDP',func=Pin.PWRIN,do_erc=True),
            Pin(num='19',name='LB1',func=Pin.OUTPUT,do_erc=True),
            Pin(num='29',name='VCC_IO',func=Pin.PWRIN,do_erc=True)])])
