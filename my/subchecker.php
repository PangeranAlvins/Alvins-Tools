<?php
/*
Pangeran Alvins
*/
// Started //

// Msg Usage //
if ( $argc < 2 ){
  print " __     __      _______    _                    
 \ \   / /     |__   __|  | |                   
  \ \_/ /__  _   _| |_   _| |__   ___           
   \   / _ \| | | | | | | | '_ \ / _ \          
    | | (_) | |_| | | |_| | |_) |  __/          
   _|_|\___/ \__,_|_|\__,_|_.__/ \___|          
  / ____|     | |                 (_) |         
 | (___  _   _| |__  ___  ___ _ __ _| |__   ___ 
  \___ \| | | | '_ \/ __|/ __| '__| | '_ \ / _ \
  ____) | |_| | |_) \__ \ (__| |  | | |_) |  __/
 |_____/ \__,_|_.__/|___/\___|_|  |_|_.__/ \___|

";
  exit( "[??] Youtube Subscribe Checker [??]\n[??]   Pangeran Alvins   [??]\n----------------------------------\nPerintah: subcheker.php <URL YouToube>\n\n\n" );
}
// Config //
  print " __     __      _______    _                    
 \ \   / /     |__   __|  | |                   
  \ \_/ /__  _   _| |_   _| |__   ___           
   \   / _ \| | | | | | | | '_ \ / _ \          
    | | (_) | |_| | | |_| | |_) |  __/          
   _|_|\___/ \__,_|_|\__,_|_.__/ \___|          
  / ____|     | |                 (_) |         
 | (___  _   _| |__  ___  ___ _ __ _| |__   ___ 
  \___ \| | | | '_ \/ __|/ __| '__| | '_ \ / _ \
  ____) | |_| | |_) \__ \ (__| |  | | |_) |  __/
 |_____/ \__,_|_.__/|___/\___|_|  |_|_.__/ \___|

";
echo "\033[1;37m[\033[1;32m+\033[1;37m] Link Channel: \033[1;32m ".$argv[1]."\n";
echo "\033[1;37m[\033[1;32m*\033[1;37m] Tools Berjalan:\033[1;32m Started\n";
echo "\033[1;32m[\033[1;37m~\033[1;32m] Proses Mulai: \033[1;33m".date("Y/m/d H:i:s")."\n";
echo "\033[1;32m[\033[1;37m@\033[1;32m] Refres Waktu Detik[\033[1;37m5\033[1;32m]\033[1;37m Seconds\n\n";
while (1){
  $channel = $argv[1];
  $t = file_get_contents($channel);
  $pattern = '/yt-uix-tooltip" title="(.*)" tabindex/';
  preg_match($pattern, $t, $matches, PREG_OFFSET_CAPTURE);
  echo "\033[1;32m[\033[1;37m+\033[1;32m]\033[1;37m Jumblah >>>\033[1;32m ".$matches[1][0]." \033[1;37m<<< \033[1;32mSubscribers\n";
  for($s=5; $s >=0; $s--){
  echo "Sedang Berjalan... [ ${s}s ] \r";
  sleep(1);
  }
  echo "";
}
?>
