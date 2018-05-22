class goodweConfig :
   GOODWE_SYSTEM_ID = 'goodwe_system_id'
   GOODWE_USER_ID = 'goodwe_user_id'
   GOODWE_PASSWORD = 'goodwe_password'
   PVOUTPUT_SYSTEM_ID = 'pvoutput_system_id'
   PVOUTPUT_API = 'pvoutput_api'
   CSV_DIR = 'csv_dir'
   SPLINE_FIT = 'spline_fit'
   INPUT_SOURCE = 'input_source'

   #--------------------------------------------------------------------------
   def __init__( self, configFile):
   # Initialization of the goodweConfig class. This class read the config
   # file and stores these.

      # These URLs should be okay for Goodwe-power and PVoutput.org (and yes,
      # there is a spelling error in the goodwe URL).
      self.goodwe_url = 'http://goodwe-power.com/PowerStationPlatform/PowerStationReport/InventerDetail'
      self.goodwe_loginUrl = 'http://goodwe-power.com/User/Login'
      self.pvoutput_url = 'http://pvoutput.org/service/r2/addstatus.jsp'
      self.spline_fit = False
      
      with open( configFile) as fp:
         for line in fp:
	    line = line[:line.find('#')]
	    line = line.replace(' ', '')
	    line = line.replace('=', '')
	    line = line.replace(':', '')
	    line = line.replace('\'', '')
	    
	    if self.GOODWE_SYSTEM_ID in line:
	       self.goodwe_system_id = line.replace(self.GOODWE_SYSTEM_ID, '')
	    if self.GOODWE_USER_ID in line:
	       self.goodwe_user_id = line.replace(self.GOODWE_USER_ID, '')
	    if self.GOODWE_PASSWORD in line:
	       self.goodwe_password = line.replace(self.GOODWE_PASSWORD, '')
	    if self.PVOUTPUT_SYSTEM_ID in line:
	       self.pvoutput_system_id = line.replace(self.PVOUTPUT_SYSTEM_ID, '')
	    if self.PVOUTPUT_API in line:
	       self.pvoutput_api = line.replace(self.PVOUTPUT_API, '')
	    if self.CSV_DIR in line:
	       self.csv_dir = line.replace(self.CSV_DIR, '')
	    if self.SPLINE_FIT in line:
               self.spline_fit = line.replace(self.SPLINE_FIT, '') == "True"
	    if self.INPUT_SOURCE in line:
               self.input_source = line.replace(self.INPUT_SOURCE, '')

   #--------------------------------------------------------------------------
   def to_string( self):
   # Prints a string representation fo the class
   #
      print "Goodwe URL: (" + self.goodwe_url + ")"
      print "Goodwe Login URL: (" + self.goodwe_loginUrl + ")"
      print self.GOODWE_SYSTEM_ID + " (" + self.goodwe_system_id + ")"
      print self.GOODWE_USER_ID + " (" + self.goodwe_user_id + ")"  
      print self.GOODWE_PASSWORD + " (" + self.goodwe_password + ")"  
      print "PVOutput upload URL: (" + self.pvoutput_url + ")"
      print self.PVOUTPUT_SYSTEM_ID + " (" + self.pvoutput_system_id + ")"
      print self.PVOUTPUT_API + " (" + self.pvoutput_api + ")"
      print self.CSV_DIR + " (" + self.csv_dir + ")"
      print self.SPLINE_FIT + " (" + str(self.spline_fit) + ")"
      print self.INPUT_SOURCE + " (" + str(self.input_source) + ")"
      
            
   #--------------------------------------------------------------------------
   def get_goodwe_system_id( self):
   # Returns the goodwe_system_id
   #
      return self.goodwe_system_id


   #--------------------------------------------------------------------------
   def get_goodwe_user_id( self):
   # Returns the goodwe_user_id
   #
      return self.goodwe_user_id


   #--------------------------------------------------------------------------
   def get_goodwe_password( self):
   # Returns the goodwe_password
   #
      return self.goodwe_password


   #--------------------------------------------------------------------------
   def get_pvoutput_system_id( self):
   # Returns the pvoutput_system_id
   #
      return self.pvoutput_system_id


   #--------------------------------------------------------------------------
   def get_pvoutput_api( self):
   # Returns the pvoutput_api
   #
      return self.pvoutput_api


   #--------------------------------------------------------------------------
   def get_csv_dir( self):
   # Returns the csv_dir
   #
      return self.csv_dir


   #--------------------------------------------------------------------------
   def get_goodwe_url( self):
   # Returns the goodwe_url
   #
      return self.goodwe_url


   #--------------------------------------------------------------------------
   def get_goodwe_loginUrl( self):
   # Returns the goodwe_loginUrl
   #
      return self.goodwe_loginUrl


   #--------------------------------------------------------------------------
   def get_pvoutput_url( self):
   # Returns the pvoutput_url
   #
      return self.pvoutput_url


   #--------------------------------------------------------------------------
   def get_spline_fit( self):
   # Returns the pvoutput_url
   #
      return self.spline_fit


   #--------------------------------------------------------------------------
   def get_input_source( self):
   # Returns the input_source
   #
      return self.input_source

#---------------- End of file ------------------------------------------------
