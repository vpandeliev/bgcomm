var pathArray = window.location.pathname.split( '/' );
var newPathname1 = "";
var newPathname2 = "";
for ( i = 0; i < pathArray.length; i++ ) {
switch (pathArray[i]) {
	case 'en':
	newPathname1 += "/";
	newPathname1 += 'bg';
	newPathname2 += "/";
	newPathname2 += 'fr';
	break;
	case 'bg':
	newPathname1 += "/";
	newPathname1 += 'en';
	newPathname2 += "/";
	newPathname2 += 'fr';
	break;
	case 'fr':
	newPathname1 += "/";
	newPathname1 += 'bg';
	newPathname2 += "/";
	newPathname2 += 'en';
	break;
	default:
	newPathname1 += "/";
	newPathname1 += pathArray[i];
	newPathname2 += "/";
	newPathname2 += pathArray[i];
	
}
}
newPathname1 = newPathname1.slice(1);
newPathname2 = newPathname2.slice(1);
document.getElementById("tr1").href = newPathname2;
document.getElementById("tr2").href = newPathname1;
