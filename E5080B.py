import pyvisa


class VNA_E5080B():

    def __init__( self, address ):
        self.address = address
        # Initialize VISA resource manager
        rm = pyvisa.ResourceManager()

        try:
            vna = rm.open_resource( address )
            vna.close()
            self.vna = vna

        except pyvisa.VisaIOError as e:
            print(f"VISA IO Error: {e}")

    def _set_linfreq_range( self, start, stop ):
        # print()
        vna.write(':SENS1:FREQ:START 1E9')
        vna.write(':SENS1:FREQ:STOP 3E9')


if __name__ == '__main__':

    vna = VNA_E5080B("TCPIP0::192.168.1.78::inst0::INSTR")
    
    # Set start and stop frequencies
    vna._set_linfreq_range( 1e9, 3e9)
    
    # Define a measurement (e.g., S11)
    vna.write(':CALC1:PAR:DEF "MyMeas",S11')
    
    # Select the defined measurement
    vna.write(':CALC1:PAR:SEL "MyMeas"')

    # Perform a single sweep and wait for completion
    vna.write(':INIT1:IMM; *OPC?')
    
    # Read and print the measurement data
    data = vna.query(':CALC1:DATA? SDATA')
    print(data)    
    
    # Check for errors
    error = vna.query('SYST:ERR?')
    if error != '+0,"No error"':
        print(f"Instrument Error: {error}")

    vna.close()



