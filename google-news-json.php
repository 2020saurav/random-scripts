<?php

$result=array();

$html = file_get_contents("https://news.google.co.in/news/section?pz=1&cf=all&topic=n");
$head = strpos($html, 'class="blended-wrapper blended-wrapper-first blended-wrapper-last esc-wrapper"');
$html = substr($html, $head);
$head = strpos($html, 'class="esc-layout-article-cell"');
$html = substr($html, $head);
$head = strpos($html, '<span class="titletext">')+24;
$html = substr($html, $head);
$tail = strpos($html, '<');
$headline = substr($html, 0, $tail );
$headline = addslashes(str_replace("&quot;", "\"", $headline));
//echo $news."<br/>";
$head = strpos($html,'class="esc-lead-snippet-wrapper"' )+33;
$html = substr($html, $head);
$tail = strpos($html, '<');
$description = substr($html, 0, $tail );
$description = addslashes(str_replace("&quot;", "\"", $description));
//echo $news."<br/><br/>";
$bundle = array("headline" => $headline, "description" => $description);$result[] = $bundle;$head = strpos($html,'class="blended-wrapper esc-wrapper"');
$html = substr($html, $head);

while(strpos($html, 'class="blended-wrapper esc-wrapper"')!==FALSE)
{
	$head = strpos($html, 'class="esc-layout-article-cell"');
	$html = substr($html, $head);
	$head = strpos($html, '<span class="titletext">')+24;
	$html = substr($html, $head);
	$tail = strpos($html, '<');
	$headline = substr($html, 0, $tail );
	$headline = addslashes(str_replace("&quot;", "\"", $headline));
	//echo $news."<br/>";
	$head = strpos($html,'class="esc-lead-snippet-wrapper"' )+33;
	$html = substr($html, $head);
	$tail = strpos($html, '<');
	$description = substr($html, 0, $tail );
	$description = addslashes(str_replace("&quot;", "\"", $description));
	
	//echo $news."<br/><br/>";
	$bundle = array("headline" => $headline, "description" => $description);

	$result[] = $bundle;
	
	$head = strpos($html,'class="blended-wrapper esc-wrapper"');
	$html = substr($html, $head);
	
}

$head = strpos($html, 'class="blended-wrapper blended-wrapper-last esc-wrapper"');
$html = substr($html, $head);
$head = strpos($html, '<span class="titletext">')+24;
$html = substr($html, $head);
$tail = strpos($html, '<');
$headline = substr($html, 0, $tail );
$headline = addslashes(str_replace("&quot;", "\"", $headline));
//echo $news."<br/>";
$head = strpos($html,'class="esc-lead-snippet-wrapper"' )+33;
$html = substr($html, $head);
$tail = strpos($html, '<');
$description = substr($html, 0, $tail );
$description = addslashes(str_replace("&quot;", "\"", $description));
//echo $news."<br/><br/>";
$bundle = array("headline" => $headline, "description" => $description);$result[] = $bundle;$head = strpos($html,'class="blended-wrapper esc-wrapper"');
$html = substr($html, $head);

$arr = array("news" => $result);
print json_encode($arr);

?>