import readGoodwe
import goodweConfig
import goodweData
import pvoutput
import csvoutput
import processData
import time
import getpass
import os

def mainloop( goodwe, pvoutput, csv, process):
# Main processing loop
#
   # Do for ever.
   while True:
      interval = 4.0*60
      try: # Read Goodwe data from goodwe-power.com
         gw = goodwe.read_sample_data()
      except Exception, arg:
         interval = 1.0*60
         print "Read data Error: " + str(arg)
      else:
         if goodwe.is_online():
            # write CSV file
            csv.write_data( gw)
            process.processSample( gw)
         else:
            # Wait for the inverter to come online
            print "Inverter is not online: " + gw.to_string()
            interval = 10.0*60
            csv.reset()
            process.reset()
	 
      # Wait for the next sample
      print "sleep " + str(interval) + " seconds before next sample"
      time.sleep(interval)



if __name__ == "__main__":
# Main entry point for the Goodwe to PVoutput logging script. Creates the
# objects needed and sets the URL and system IDs. These are read from the
# config file in ${HOME}/.goodwe2pvoutput
#
   home = os.path.expanduser('~')
   config = goodweConfig.goodweConfig(home+'/.goodwe2pvoutput')
   config.to_string()

   pvoutput = pvoutput.pvoutput( config.get_pvoutput_url(),
                                 config.get_pvoutput_system_id(),
                                 config.get_pvoutput_api())
   csv = csvoutput.csvoutput( config.get_csv_dir(), 'Goodwe_PV_data')

   goodwe = readGoodwe.readGoodwe( config.get_goodwe_url(),
                                   config.get_goodwe_loginUrl(),
                                   config.get_goodwe_system_id())
   # Login to Goodwe-power.com
   goodwe.login( config.get_goodwe_user_id(), config.get_goodwe_password())

   process = processData.processData( pvoutput)

   # Perform main loop
   mainloop( goodwe, pvoutput, csv, process)


#---------------- End of file ------------------------------------------------
