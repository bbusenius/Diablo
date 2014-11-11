<?php 

$foo = array (
   0 => array 
   ( 
      'id' => 2386211, 
      'status' => 'AVAILABLE', 
      'location' => 'Crerar, Bookstacks', 
      'reserve' => 'N', 
      'callnumber' => ' Q1.N2', 
      'foobar' => array 
      ( 
         'one' => 1, 
         'two' => 2, 
         'three' => 3, 
         'four' => 4, 
      ),
      'availability' => True, 
   ),
   1 => array 
   ( 
      'id' => 2386211, 
      'status' => 'MISSING',
      'test' => array(1,2,3,4,5), 
      'location' => 'Crerar, Bookstacks', 
      'reserve' => 'N',
      'testnull' => null, 
      'callnumber' => ' Q1.N2', 
      'availability' => False, 
   ),
   2 => array 
   ( 
      'id' => 2386211, 
      'status' => 'AVAILABLE', 
      'location' => 'Crerar, Bookstacks', 
      'reserve' => 'N', 
      'callnumber' => ' Q1.N2', 
      'availability' => True, 
   ),
   3 => array 
   ( 
      'id' => 2386211, 
      'status' => 'AVAILABLE', 
      'location' => 'Special Collections, Crerar Rare Books', 
      'reserve' => 'N', 
      'callnumber' => ' Q1.N2', 
      'availability' => True, 
   ),

);
 
echo serialize($foo);

?>

