html = r"""<!DOCTYPE html>
    <meta http-equiv="x-ua-compatible" content="IE=edge" />

    <!--[if lt IE 7]><html class="no-js lt-ie10 lt-ie9 lt-ie8 lt-ie7" lang="en"> <![endif]-->
    <!--[if IE 7]><html class="no-js lt-ie10 lt-ie9 lt-ie8" lang="en"> <![endif]-->
    <!--[if IE 8]><html class="no-js lt-ie10 lt-ie9" lang="en"> <![endif]-->
    <!--[if IE 9]><html class="no-js lt-ie10" lang="en"> <![endif]-->
    <!--[if gt IE 9]><!--> <html class="no-js" lang="en"> <!--<![endif]-->
    <head>
        <link rel="stylesheet" href="fara_ws/r/1381/files/static/v17/theme_table.css" type="text/css" />  
    <meta charset="utf-8">  
    <title>Active Foreign Principals by Country or Location  as of 05&#x2F;02&#x2F;2021</title>
    <link rel="stylesheet" href="/i/app_ui/css/Core.min.css?v=5.1.2.00.09" type="text/css" />
    <link rel="stylesheet" href="/i/app_ui/css/Theme-Standard.min.css?v=5.1.2.00.09" type="text/css" />
    <link rel="stylesheet" href="/i/libraries/jquery-ui/1.10.4/themes/base/jquery-ui.min.css?v=5.1.2.00.09" type="text/css" />

    <link rel="stylesheet" href="/i/libraries/font-apex/1.0/css/font-apex.min.css?v=5.1.2.00.09" type="text/css" />
    <link rel="stylesheet" href="/i/themes/theme_42/1.1/css/Core.min.css?v=5.1.2.00.09" type="text/css" />

    
    <link rel="stylesheet" href="/i/themes/theme_42/1.1/css/Vita.min.css?v=5.1.2.00.09" type="text/css" />

    
    
    <link rel="shortcut icon" href="/i/favicon.ico">
    <link rel="icon" sizes="16x16" href="/i/favicon-16x16.png">
    <link rel="icon" sizes="32x32" href="/i/favicon-32x32.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/i/favicon-180x180.png">
    
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta http-equiv="Pragma" content="no-cache" /><meta http-equiv="Expires" content="-1" /><meta http-equiv="Cache-Control" content="no-cache" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no"/>
        <title>FARA EFile</title>
    <meta name="dc.title" content="" />
    <meta name="dc.description" scheme="ISO639" content="" />
    <meta name="dc.creator" scheme="ISO639" content="National Security Division, U.S. Department of Justice" />
    <meta name="dc.language" scheme="ISO639" content="en-us"/>
    <meta name="dc.date.created" content="2011-03-18"/>
        
    <script type="text/javascript" src="/ords/ruxitagentjs_ICA27SVfjqrux_10213210407103252.js" data-dtconfig="app=9d9f6cc2247707ff|rcdec=1209600000|featureHash=ICA27SVfjqrux|vcv=2|rdnt=1|uxrgce=1|srcss=1|bp=2|srmcrv=10|cuc=6ywe117d|mel=100000|dpvc=1|ssv=4|lastModification=1619325160286|dtVersion=10213210407103252|srmcrl=1|tp=500,50,0,1|uxdcw=1500|vs=2|agentUri=/ords/ruxitagentjs_ICA27SVfjqrux_10213210407103252.js|reportUrl=/ords/rb_e90d824a-fd6d-4619-b98c-30350634b234|rid=RID_1953774470|rpid=-1994652243|domain=fara.gov"></script><link rel="stylesheet" href="fara_ws/r/1381/files/static/v17/style.css" type="text/css" media="all" />
    <link rel="stylesheet" href="fara_ws/r/1381/files/static/v17/nsd-style.css" type="text/css" />
    <link rel="stylesheet" href="fara_ws/r/1381/files/static/v17/tiles-menu.css" type="text/css">    
    <script type="text/javascript" src="fara_ws/r/1381/files/static/v17/jquery.min.js"></script>
    <script type="text/javascript" language="Javascript"  src="fara_ws/r/1381/files/static/v17/justiceiso.js"> </script>

    <link rel="stylesheet" href="fara_ws/r/1381/files/static/v17/search-template.css" type="text/css">      

    <link type="text/css" rel="stylesheet" href="fara_ws/r/1381/files/static/v17/DOJv2.css" media="all" />       
    
    
    <script>function MM_swapImgRestore() { //v3.0
    var i,x,a=document.MM_sr; for(i=0;a&&i<a.length&&(x=a[i])&&x.oSrc;i++) x.src=x.oSrc;
    }
    function MM_preloadImages() { //v3.0
    var d=document; if(d.images){ if(!d.MM_p) d.MM_p=new Array();
        var i,j=d.MM_p.length,a=MM_preloadImages.arguments; for(i=0; i<a.length; i++)
        if (a[i].indexOf("#")!=0){ d.MM_p[j]=new Image; d.MM_p[j++].src=a[i];}}
    }

    function MM_findObj(n, d) { //v4.01
    var p,i,x;  if(!d) d=document; if((p=n.indexOf("?"))>0&&parent.frames.length) {
        d=parent.frames[n.substring(p+1)].document; n=n.substring(0,p);}
    if(!(x=d[n])&&d.all) x=d.all[n]; for (i=0;!x&&i<d.forms.length;i++) x=d.forms[i][n];
    for(i=0;!x&&d.layers&&i<d.layers.length;i++) x=MM_findObj(n,d.layers[i].document);
    if(!x && d.getElementById) x=d.getElementById(n); return x;
    }

    function MM_swapImage() { //v3.0
    var i,j=0,x,a=MM_swapImage.arguments; document.MM_sr=new Array; for(i=0;i<(a.length-2);i+=3)
    if ((x=MM_findObj(a[i]))!=null){document.MM_sr[j++]=x; if(!x.oSrc) x.oSrc=x.src; x.src=a[i+2];}
    }

    $(document).ready(function(){	
        //Caption Sliding (Partially Hidden to Visible)
        $('.boxgrid.caption').hover(function(){
            $(".cover", this).stop().animate({top:'0px'},{queue:false,duration:160});
        }, function() {
            $(".cover", this).stop().animate({top:'100px'},{queue:false,duration:160});
        });

    $('nav').css({"background-color":"white"});

    });
        </script>
        
    </head>



    <!--[if IEMobile 7]><html class="no-js ie iem7 not-responsive" lang="en" dir="ltr"><![endif]-->
    <!--[if lte IE 6]><html class="no-js ie lt-ie9 lt-ie8 lt-ie7 not-responsive" lang="en" dir="ltr"><![endif]-->
    <!--[if (IE 7)&(!IEMobile)]><html class="no-js ie lt-ie9 lt-ie8 not-responsive" lang="en" dir="ltr"><![endif]-->
    <!--[if IE 8]><html class="no-js ie lt-ie9 not-responsive" lang="en" dir="ltr"><![endif]-->
    <!--[if (gte IE 9)|(gt IEMobile 7)]><html class="no-js ie responsive" lang="en" dir="ltr" prefix="og: http://ogp.me/ns# article: http://ogp.me/ns/article# book: http://ogp.me/ns/book# profile: http://ogp.me/ns/profile# video: http://ogp.me/ns/video# product: http://ogp.me/ns/product# content: http://purl.org/rss/1.0/modules/content/ dc: http://purl.org/dc/terms/ foaf: http://xmlns.com/foaf/0.1/ rdfs: http://www.w3.org/2000/01/rdf-schema# sioc: http://rdfs.org/sioc/ns# sioct: http://rdfs.org/sioc/types# skos: http://www.w3.org/2004/02/skos/core# xsd: http://www.w3.org/2001/XMLSchema#"><![endif]-->
    <!--[if !IE]><!--><html class="no-js responsive" lang="en" dir="ltr" prefix="og: http://ogp.me/ns# article: http://ogp.me/ns/article# book: http://ogp.me/ns/book# profile: http://ogp.me/ns/profile# video: http://ogp.me/ns/video# product: http://ogp.me/ns/product# content: http://purl.org/rss/1.0/modules/content/ dc: http://purl.org/dc/terms/ foaf: http://xmlns.com/foaf/0.1/ rdfs: http://www.w3.org/2000/01/rdf-schema# sioc: http://rdfs.org/sioc/ns# sioct: http://rdfs.org/sioc/types# skos: http://www.w3.org/2004/02/skos/core# xsd: http://www.w3.org/2001/XMLSchema#"><!--<![endif]-->
    <head>
    <title>Foreign Agents Registration Act | Department of Justice</title>
    <!--[if IE]><![endif]-->
    <meta charset="utf-8" />
    <link rel="apple-touch-icon-precomposed" href="https://www.justice.gov/sites/all/themes/justice/apple-touch-icon-precomposed-144x144.png" sizes="144x144" />
    <link rel="apple-touch-icon-precomposed" href="https://www.justice.gov/sites/all/themes/justice/apple-touch-icon-precomposed.png" />
    <link rel="apple-touch-icon-precomposed" href="https://www.justice.gov/sites/all/themes/justice/apple-touch-icon-precomposed-72x72.png" sizes="72x72" />
    <meta http-equiv="cleartype" content="on" />
    <meta name="MobileOptimized" content="width" />
    <meta name="HandheldFriendly" content="true" />
    <link rel="profile" href="http://www.w3.org/1999/xhtml/vocab" />
    <link rel="shortcut icon" href="https://www.justice.gov/sites/default/files/favicon.png" type="image/png" />
    <script async="async" id="_fed_an_ua_tag" src="https://dap.digitalgov.gov/Universal-Federated-Analytics-Min.js?agency=DOJ&amp;sp=find&amp;yt=true&amp;subagency=nsd-fara"></script>
    <link rel="apple-touch-icon-precomposed" href="https://www.justice.gov/sites/all/themes/justice/apple-touch-icon-precomposed-114x114.png" sizes="114x114" />
    <meta name="generator" content="Drupal 7 (http://drupal.org)" />
    <meta name="viewport" content="width=device-width" />
    <link rel="canonical" href="https://www.justice.gov/nsd-fara" />



    <![endif]-->
    </head>
    <body x-ms-format-detection="none" class="html not-front not-logged-in page-node page-node- page-node-948656 node-type-organization og-context og-context-node og-context-node-948656 i18n-en section-nsd-fara one-sidebar sidebar-first og-context-foreign-agents-registration-act">
    <a id="skip-link" href="#main-content" class="element-invisible element-focusable">Skip to main content</a>
        <div class="l-page panelized">
    <a name="page-top"></a>
    <div class="l-header-wrapper">
        <header class="l-header" role="banner">
        <div class="l-branding site-branding">
                    <a href="https://www.justice.gov/" title="The United States Department of Justice" rel="home" class="site-branding__logo desktop"><img src="https://www.justice.gov/sites/default/files/header-logo_bronze-resized-5-2.png" alt="The United States Department of Justice" /></a>
            <a href="/" title="The United States Department of Justice" rel="home" class="site-branding__logo mobile"><img src="https://www.justice.gov/sites/default/files/header-logo-mobile_bronze5.png" alt="The United States Department of Justice" /></a>
            
                </div>
            <div class="l-region l-region--header">
        <div id="block-usasearch-hosted-form" class="block block--usasearch-hosted block--usasearch-hosted-form">
            <div class="block__content">
        <form class="usasearch-hosted-box" action="https://search.justice.gov/search" method="get" id="usasearch-hosted-box" accept-charset="UTF-8"><div><div class="container-inline">
        <h2 class="element-invisible">Search form</h2>
        <div class="form-item form-type-textfield form-item-usasearch-hosted-box">
    <label class="element-invisible" for="edit-usasearch-hosted-box--2">Search </label>
    <input class="usagov-search-autocomplete ui-autocomplete-input ui-corner-all form-text" autocomplete="off" type="text" name="query" placeholder="Search this site" id="edit-usasearch-hosted-box--2" value="" size="15" maxlength="128" /> 
    </div>
    <div class="form-actions form-wrapper" id="edit-actions"><input type="submit" id="edit-submit" name="op" value="Search" class="form-submit" /></div><input type="hidden" name="affiliate" value="justice" />
    </div>
    </div></form>  </div>
    </div>
    </div>

        </header>
        <div class="l-region l-region--navigation">
        <div id="block-nice-menus-1" class="block block--nice-menus block--nice-menus-1">
            <h2 class="block__title"><span class="nice-menu-hide-title">Main menu</span></h2>
        <div class="block__content">
        <ul class="nice-menu nice-menu-down nice-menu-main-menu" id="nice-menu-1"><li class="menu-1258 menu-path-front first odd "><a href="https://www.justice.gov/" title="">Home</a></li>
    <li class="menu-1259 menuparent  menu-path-node-82626  even "><a href="/about" title="">About</a><ul><li class="menu-9686 menu-path-node-1652 first odd "><a href="https://www.justice.gov/ag" title="">The Attorney General</a></li>
    <li class="menu-1267 menu-path-node-82606  even "><a href="https://www.justice.gov/doj/budget-and-performance" title="">Budget &amp; Performance</a></li>
    <li class="menu-51706 menu-path-node-632231  odd "><a href="https://www.justice.gov/about/history" title="">History</a></li>
    <li class="menu-89781 menu-path-node-1666  even last"><a href="https://www.justice.gov/opcl" title="">Privacy Program</a></li>
    </ul></li>
    <li class="menu-1260 menuparent  menu-path-node-33666-chart  odd "><a href="https://www.justice.gov/agencies/chart" title="">Agencies</a><ul><li class="menu-90596 menu-path-node-33666-chart first odd "><a href="https://www.justice.gov/agencies/chart" title="">Organizational Chart</a></li>
    <li class="menu-90591 menu-path-node-924706  even last"><a href="https://www.justice.gov/agencies/alphabetical-listing-components-programs-initiatives" title="">Alphabetical Listing</a></li>
    </ul></li>
    <li class="menu-1262 menuparent  menu-path-node-82271  even "><a href="https://www.justice.gov/resources" title="">Resources</a><ul><li class="menu-92026 menu-path-node-82476 first odd "><a href="https://www.justice.gov/grants" title="">Grants</a></li>
    <li class="menu-1261 menu-path-node-82486  even "><a href="https://www.justice.gov/business" title="">Business</a></li>
    <li class="menu-1272 menu-path-justicegov-forms  odd "><a href="http://www.justice.gov/forms" title="">Forms</a></li>
    <li class="menu-1273 menu-path-node-643761  even "><a href="https://www.justice.gov/publications" title="">Publications</a></li>
    <li class="menu-5306 menu-path-largecases  odd last"><a href="https://www.justice.gov/largecases" title="">Information for Victims in Large Cases</a></li>
    </ul></li>
    <li class="menu-1263 menuparent  menu-path-node-24871  odd "><a href="https://www.justice.gov/briefing-room" title="">News</a><ul><li class="menu-1276 menu-path-node-780336 first odd "><a href="https://www.justice.gov/news" title="">Press Releases</a></li>
    <li class="menu-1278 menu-path-node-890381  even "><a href="https://www.justice.gov/public-schedule" title="">Public Schedule</a></li>
    <li class="menu-1279 menu-path-node-665661  odd "><a href="https://www.justice.gov/videos" title="">Videos</a></li>
    <li class="menu-1280 menu-path-opa-galleries  even last"><a href="https://www.justice.gov/opa/galleries" title="">Photos</a></li>
    </ul></li>
    <li class="menu-92596 menuparent  menu-path-node-865991 active-trail  even "><a href="https://www.justice.gov/careers" title="">Careers</a><ul><li class="menu-2925 menu-path-node-3643 first odd "><a href="https://www.justice.gov/legal-careers">Legal Careers</a></li>
    <li class="menu-3650 menu-path-node-796646  even "><a href="https://www.justice.gov/careers/veteran-recruitment" title="">Veteran Recruitment</a></li>
    <li class="menu-92601 menu-path-node-6001  odd last"><a href="https://www.justice.gov/careers/disability-hiring" title="">Disability Hiring</a></li>
    </ul></li>
    <li class="menu-1265 menu-path-node-82636  odd last"><a href="https://www.justice.gov/contact-us" title="">Contact</a></li>
    </ul>
    </div>
    </div>
    </div>
    </div>

    <div class="l-lower">
        
        <div class="l-main-wrapper">
        <div class="l-main">
            <div class="site-info">
            <h2 class="element-invisible">You are here</h2><div class="breadcrumb">
            
            <span class="bread">
            <a href="https://www.justice.gov/">Home</a> 
    » <a href="https://www.justice.gov/nsd-fara">Foreign Agents 
    Registration Act</a>
    </span>
    </div>        </div>

                    <div class="pre-content clearfix">
                <div class="l-region l-region--pre-content">
        <div id="block-doj-sharing-doj-sharing" class="block block--doj-sharing block--doj-sharing-doj-sharing">
            <div class="block__content">
        <div class="doj-sharing" style="display:none;">
    <a id="doj-sharing-toggle" tabindex="0" title="Choose a social sharing platform">
        Share  </a>
    <ul>
        <li>
        <a href="http://www.facebook.com/sharer/sharer.php?u=https://www.justice.gov/nsd-fara" target="_blank" title="Share on Facebook" data-event-label="Share on Facebook">Facebook</a>
        </li>
        <li>
        <a href="http://twitter.com/intent/tweet?url=https://www.justice.gov/nsd-fara&amp;text=Foreign%20Agents%20Registration%20Act" target="_blank" title="Share on Twitter" data-event-label="Share on Twitter">Twitter</a>
        </li>
        <li>
        <a href="https://plus.google.com/share?url=https://www.justice.gov/nsd-fara" target="_blank" title="Share on Google+" data-event-label="Share on Google+">Google+</a>
        </li>
        <li>
        <a href="http://www.linkedin.com/shareArticle?mini=true&amp;url=https://www.justice.gov/nsd-fara&amp;title=Foreign%20Agents%20Registration%20Act" target="_blank" title="Share on LinkedIn" data-event-label="Share on LinkedIn">LinkedIn</a>
        </li>
        <li>
        <a href="http://digg.com/submit?url=https://www.justice.gov/nsd-fara&amp;title=Foreign%20Agents%20Registration%20Act" target="_blank" title="Share on Digg" data-event-label="Share on Digg">Digg</a>
        </li>
        <li>
        <a href="http://reddit.com/submit?url=https://www.justice.gov/nsd-fara&amp;title=Foreign%20Agents%20Registration%20Act" target="_blank" title="Share on Reddit" data-event-label="Share on Reddit">Reddit</a>
        </li>
        <li>
        <a href="http://www.stumbleupon.com/submit?url=https://www.justice.gov/nsd-fara&amp;title=Foreign%20Agents%20Registration%20Act" target="_blank" title="Share on StumbleUpon" data-event-label="Share on StumbleUpon">StumbleUpon</a>
        </li>
        <li>
        <a href="http://pinterest.com/pin/create/button/?url=https://www.justice.gov/nsd-fara&amp;media=https%3A//www.justice.gov/sites/all/modules/features/doj_sharing/images/doj-seal-pin.png&amp;title=Foreign%20Agents%20Registration%20Act" target="_blank" title="Share on Pinterest" data-event-label="Share on Pinterest">Pinterest</a>
        </li>
        <li>
        <a href="mailto:?to=&body=https://www.justice.gov/nsd-fara&subject=Foreign%20Agents%20Registration%20Act" title="Email" data-event-label="Email">Email</a>
        </li>
    </ul>
    </div>
    </div>
    </div>
    </div>
            </div>
            
            <aside class="l-region l-region--sidebar-first">
        <div id="block-og-menu-og-single-menu-block" class="block block--og-menu block--og-menu-og-single-menu-block">
            <h2 class="block__title">Foreign Agents Registration Act</h2>
        <div class="block__content">
    <UL class="menu">
    <LI class="first leaf"><A title="" href="https://www.justice.gov/nsd-fara">FARA 
    Home</A></LI>
    <LI class="collapsed"><A title="" href="https://www.justice.gov/nsd-fara/legal-authority">Legal 
    Authority</A></LI>
            <LI class="leaf"><A title="" href="https://www.justice.gov/nsd-fara/fara-enforcement">Enforcement</A></LI>
        <LI class="leaf"><A title="" href="https://www.justice.gov/nsd-fara/recent-cases">Recent Cases</A></LI>
    <LI class="leaf"><A title=""  href="https://www.justice.gov/nsd-fara/fara-efile">FARA 
    eFile</A></LI>
    <LI class="leaf"><A title="" href="https://www.justice.gov/nsd-fara/advisory-opinions">Advisory 
    Opinions</A></LI>
    <LI class="collapsed"><A title="" href="https://www.justice.gov/nsd-fara/fara-frequently-asked-questions">Frequently 
    Asked Questions</A></LI>
    <LI class="leaf"><A title="" href="https://www.justice.gov/nsd-fara/fara-forms">Registration 
    Forms</A></LI>
    <LI class="leaf"><A title="" href="https://www.justice.gov/nsd-fara/fara-fee-schedule">Fee 
    Schedule</A></LI>

        
    <li class="expanded active-trail"><a title="" class="active-trail active" href="f?p=1381:1">Browse Filings</a>
        <ul class="menu">
            <li class="first leaf"><a title="" href="f?p=1381:4">By Primary Registrant</a></li>
            <li class="leaf"><a title="" href="f?p=1381:5">By Short Form Registrant</a></li>
            <li class="last leaf"><a title="" href="f?p=1381:8">By Foreign Principal</a></li>
        </ul>    
        </li>	
        
    <LI class="leaf active-trail"><a title=""  href="f?p=1235:10">Search Filings</a></li>
    <LI class="leaf"><A title="" href="https://www.justice.gov/nsd-fara/fara-reports-congress">Reports 
    to Congress</A></LI>
    <LI class="leaf"><A title="" href="https://www.justice.gov/nsd-fara/fara-contact-information">Contact 
    FARA</A></LI>
    <LI class="last leaf"><A title="" href="https://www.justice.gov/nsd/nsd-freedom-information-act">NSD 
    FOIA</A></LI></UL></DIV></DIV></ASIDE>
    <DIV class="l-content" role="main"><A tabindex="-1" id="main-content"></A>
        
        
        

    <title>Active Foreign Principals by Country or Location  as of 05&#x2F;02&#x2F;2021</title>
    <link rel="stylesheet" href="/i/app_ui/css/Core.min.css?v=5.1.2.00.09" type="text/css" />
    <link rel="stylesheet" href="/i/app_ui/css/Theme-Standard.min.css?v=5.1.2.00.09" type="text/css" />
    <link rel="stylesheet" href="/i/libraries/jquery-ui/1.10.4/themes/base/jquery-ui.min.css?v=5.1.2.00.09" type="text/css" />

    
    
    
    
        
    <link rel="shortcut icon" href="/i/favicon.ico">
    <link rel="icon" sizes="16x16" href="/i/favicon-16x16.png">
    <link rel="icon" sizes="32x32" href="/i/favicon-32x32.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/i/favicon-180x180.png">
    
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta http-equiv="Pragma" content="no-cache" /><meta http-equiv="Expires" content="-1" /><meta http-equiv="Cache-Control" content="no-cache" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no"/>
    </head>

    <body class="t-PageBody t-PageBody--hideLeft t-PageBody--hideActions no-anim   apex-side-nav apex-icons-fontapex"  id="t_PageBody">		
            
            
        <H1>Browse Filings</H1>
                


    <form action="wwv_flow.accept" method="post" name="wwv_flow" id="wwvFlowForm" novalidate >
    <input type="hidden" name="p_flow_id" value="1381" id="pFlowId" /><input type="hidden" name="p_flow_step_id" value="130" id="pFlowStepId" /><input type="hidden" name="p_instance" value="13701651723734" id="pInstance" /><input type="hidden" name="p_page_submission_id" value="50614184052926496488301704690593512567" id="pPageSubmissionId" /><input type="hidden" name="p_request" value="" id="pRequest" /><input type="hidden" name="p_reload_on_submit" value="A" id="pReloadOnSubmit" /><input type="hidden" value="50614184052926496488301704690593512567" id="pSalt" />     <ARTICLE class="node node--page node--full node--page--full" 
    role="article" typeof="foaf:Document" 
    about="/nsd-fara/fara-contact-information"><HEADER><SPAN class="rdf-meta element-hidden" 
    content="FARA Contact Information" property="dc:title"></SPAN>    </HEADER>
    <DIV class="node__content">
    <DIV class="field field--name-field-page-body field--type-text-long field--label-hidden">
    <DIV class="field__items">
    <DIV class="field__item even" style="min-width: 796px; background-color:#F8F9F4">

    <center>
    <table width="95%" cellpadding="0" cellspacing="0" border="0" summary="">
    <tr>
        <TD width="65%">
            <center>
            
            <span id="APEX_SUCCESS_MESSAGE" data-template-id="38937190782030601_S" class="apex-page-success u-hidden"></span> <span id="APEX_ERROR_MESSAGE" data-template-id="38937190782030601_E" class="apex-page-error u-hidden"></span> <TABLE cellSpacing=0 border=0>
                <TR>
                <TD width="100%"><center><div class="t-Region t-Region--scrollBody" id="R383216266043406571" >
    <div class="t-Region-header">
    <div class="t-Region-headerItems t-Region-headerItems--title">
        <h2 class="t-Region-title" id="R383216266043406571_heading">Search</h2>
    </div>
    <div class="t-Region-headerItems t-Region-headerItems--buttons"><span class="js-maximizeButtonContainer"></span></div>
    </div>
    <div class="t-Region-bodyWrap">
    <div class="t-Region-buttons t-Region-buttons--top">
        <div class="t-Region-buttons-left"></div>
        <div class="t-Region-buttons-right"></div>
    </div>
    <div class="t-Region-body">
        <div class="t-Form-fieldContainer rel-col " id="P130_CNTRY_CONTAINER"><div class="t-Form-labelContainer col col-null">
    <label for="P130_CNTRY" id="P130_CNTRY_LABEL" class="t-Form-label">Country/Location</label>
    </div>
    <div class="t-Form-inputContainer col col-null"><div class="t-Form-itemWrapper"><select  id="P130_CNTRY" name="P130_CNTRY" class="selectlist&#x20;apex-item-select" size="1" onchange="location.href&#x3D;&#x27;f&#x3F;p&#x3D;1381&#x3A;130&#x3A;13701651723734&#x3A;&#x3A;NO&#x3A;&#x3A;P130_CNTRY&#x3A;&#x27;&#x2B;encodeURIComponent&#x28;this.options&#x5B;selectedIndex&#x5D;.value&#x29;&#x3B;" ><option value="ALL" selected="selected" >All Countries&#x2F;Locations</option>
    <option value="AF">AFGHANISTAN</option>
    <option value="AL">ALBANIA</option>
    <option value="AG">ALGERIA</option>
    <option value="AO">ANGOLA</option>
    <option value="AA">ANGUILLA</option>
    <option value="AC">ANTIGUA &amp; BARBUDA</option>
    <option value="AR">ARGENTINA</option>
    <option value="AM">ARMENIA</option>
    <option value="AB">ARUBA</option>
    <option value="AS">AUSTRALIA</option>
    <option value="AU">AUSTRIA</option>
    <option value="AJ">AZERBAIJAN</option>
    <option value="BF">BAHAMAS</option>
    <option value="BA">BAHRAIN</option>
    <option value="BN">BANGLADESH</option>
    <option value="BB">BARBADOS</option>
    <option value="YL">BELARUS</option>
    <option value="BE">BELGIUM</option>
    <option value="BH">BELIZE</option>
    <option value="BK">BENIN</option>
    <option value="BD">BERMUDA</option>
    <option value="BI">BIAFRA</option>
    <option value="BL">BOLIVIA</option>
    <option value="HB">BOSNIA &amp; HERZEGOVINA</option>
    <option value="BC">BOTSWANA</option>
    <option value="BR">BRAZIL</option>
    <option value="VI">BRITISH VIRGIN ISLANDS</option>
    <option value="BX">BRUNEI</option>
    <option value="BU">BULGARIA</option>
    <option value="BZ">BURKINA FASO</option>
    <option value="BY">BURUNDI</option>
    <option value="CB">CAMBODIA</option>
    <option value="CM">CAMEROON</option>
    <option value="CA">CANADA</option>
    <option value="CJ">CAYMAN ISLANDS</option>
    <option value="CD">CHAD</option>
    <option value="CQ">CHANNEL ISLANDS</option>
    <option value="CI">CHILE</option>
    <option value="CH">CHINA</option>
    <option value="CO">COLOMBIA</option>
    <option value="CF">CONGO, DEMOCRATIC REPUBLIC OF THE</option>
    <option value="CG">CONGO, REPUBLIC OF THE</option>
    <option value="CS">COSTA RICA</option>
    <option value="IV">COTE D&#x27;IVOIRE (IVORY COAST)</option>
    <option value="CX">CROATIA</option>
    <option value="CR">CURACAO</option>
    <option value="CY">CYPRUS</option>
    <option value="ZC">CZECHIA</option>
    <option value="CZ">CZECHOSLOVAKIA</option>
    <option value="DA">DENMARK</option>
    <option value="DJ">DJIBOUTI</option>
    <option value="DO">DOMINICA</option>
    <option value="DR">DOMINICAN REPUBLIC</option>
    <option value="EC">ECUADOR</option>
    <option value="EG">EGYPT</option>
    <option value="ES">EL SALVADOR</option>
    <option value="EL">ENGLAND</option>
    <option value="EK">EQUATORIAL GUINEA</option>
    <option value="ER">ERITREA</option>
    <option value="EA">ESTONIA</option>
    <option value="ET">ETHIOPIA</option>
    <option value="FJ">FIJI</option>
    <option value="FI">FINLAND</option>
    <option value="FR">FRANCE</option>
    <option value="GB">GABON</option>
    <option value="GA">GAMBIA, THE</option>
    <option value="GG">GEORGIA</option>
    <option value="GM">GERMANY</option>
    <option value="GE">GERMANY, FEDERAL REPUBLIC OF</option>
    <option value="GH">GHANA</option>
    <option value="GI">GIBRALTAR</option>
    <option value="EN">GREAT BRITAIN</option>
    <option value="GR">GREECE</option>
    <option value="GJ">GRENADA</option>
    <option value="GT">GUATEMALA</option>
    <option value="GV">GUINEA</option>
    <option value="GY">GUYANA</option>
    <option value="HA">HAITI</option>
    <option value="HO">HONDURAS</option>
    <option value="HK">HONG KONG</option>
    <option value="HU">HUNGARY</option>
    <option value="IC">ICELAND</option>
    <option value="IN">INDIA</option>
    <option value="ID">INDONESIA</option>
    <option value="IL">INTERNATIONAL</option>
    <option value="IR">IRAN</option>
    <option value="IZ">IRAQ</option>
    <option value="EI">IRELAND</option>
    <option value="IS">ISRAEL</option>
    <option value="IT">ITALY</option>
    <option value="JM">JAMAICA</option>
    <option value="JA">JAPAN</option>
    <option value="JO">JORDAN</option>
    <option value="KZ">KAZAKHSTAN</option>
    <option value="KE">KENYA</option>
    <option value="KN">KOREA, NORTH</option>
    <option value="KS">KOREA, SOUTH</option>
    <option value="KA">KOSOVA</option>
    <option value="KU">KUWAIT</option>
    <option value="KG">KYRGYZSTAN</option>
    <option value="LA">LAOS</option>
    <option value="LV">LATVIA</option>
    <option value="LE">LEBANON</option>
    <option value="LI">LIBERIA</option>
    <option value="LY">LIBYA</option>
    <option value="LS">LIECHTENSTEIN</option>
    <option value="LU">LUXEMBOURG</option>
    <option value="MC">MACAU</option>
    <option value="MW">MACEDONIA</option>
    <option value="MI">MALAWI</option>
    <option value="MY">MALAYSIA</option>
    <option value="MV">MALDIVES</option>
    <option value="ML">MALI</option>
    <option value="MT">MALTA</option>
    <option value="MS">MARSHALL ISLANDS</option>
    <option value="MP">MAURITANIA</option>
    <option value="MR">MAURITIUS</option>
    <option value="MX">MEXICO</option>
    <option value="MK">MICRONESIA</option>
    <option value="MM">MOLDOVA</option>
    <option value="MN">MONACO</option>
    <option value="MG">MONGOLIA</option>
    <option value="NB">MONTENEGRO</option>
    <option value="MO">MOROCCO</option>
    <option value="BM">MYANMAR (BURMA)</option>
    <option value="NK">NAGORNO KARABAKH</option>
    <option value="NP">NEPAL</option>
    <option value="NL">NETHERLANDS</option>
    <option value="NA">NETHERLANDS ANTILLES</option>
    <option value="NZ">NEW ZEALAND</option>
    <option value="NU">NICARAGUA</option>
    <option value="NG">NIGER</option>
    <option value="NI">NIGERIA</option>
    <option value="NT">NORTHERN IRELAND</option>
    <option value="NO">NORWAY</option>
    <option value="OM">OMAN</option>
    <option value="PK">PAKISTAN</option>
    <option value="PZ">PALAU</option>
    <option value="PS">PALESTINE</option>
    <option value="PN">PANAMA</option>
    <option value="PP">PAPUA NEW GUINEA</option>
    <option value="PA">PARAGUAY</option>
    <option value="PE">PERU</option>
    <option value="RP">PHILIPPINES</option>
    <option value="PL">POLAND</option>
    <option value="PO">PORTUGAL</option>
    <option value="QA">QATAR</option>
    <option value="RS">REPUBLIC OF SOUTH SUDAN</option>
    <option value="RO">ROMANIA</option>
    <option value="RU">RUSSIA</option>
    <option value="RW">RWANDA</option>
    <option value="AD">SAHARAWI ARAB DEMOCRATIC REPUBLIC</option>
    <option value="ST">SAINT LUCIA</option>
    <option value="AQ">SAMOA</option>
    <option value="SA">SAUDI ARABIA</option>
    <option value="SD">SCOTLAND</option>
    <option value="SG">SENEGAL</option>
    <option value="RT">SERBIA</option>
    <option value="SE">SEYCHELLES</option>
    <option value="SL">SIERRA LEONE</option>
    <option value="SN">SINGAPORE</option>
    <option value="VK">SLOVAKIA</option>
    <option value="RV">SLOVENIA</option>
    <option value="SO">SOMALI DEMOCRATIC REPUBLIC</option>
    <option value="S3">SOMALIA</option>
    <option value="S1">SOMALILAND</option>
    <option value="SF">SOUTH AFRICA</option>
    <option value="YS">SOUTHERN YEMAN</option>
    <option value="SP">SPAIN</option>
    <option value="SR">SRI LANKA</option>
    <option value="SX">ST. BARTHELEMY</option>
    <option value="SI">ST. EUSTATIUS</option>
    <option value="MF">ST. MARTIN</option>
    <option value="SU">SUDAN</option>
    <option value="NS">SURINAME</option>
    <option value="WZ">SWAZILAND</option>
    <option value="SW">SWEDEN</option>
    <option value="SZ">SWITZERLAND</option>
    <option value="SY">SYRIA</option>
    <option value="TA">TAHITI</option>
    <option value="TW">TAIWAN</option>
    <option value="TZ">TANZANIA</option>
    <option value="TH">THAILAND</option>
    <option value="TI">TIBET</option>
    <option value="TB">TIMOR-LESTE (EAST TIMOR)</option>
    <option value="TO">TOGO</option>
    <option value="TD">TRINIDAD AND TOBAGO</option>
    <option value="TS">TUNISIA</option>
    <option value="TU">TURKEY</option>
    <option value="UG">UGANDA</option>
    <option value="UP">UKRAINE</option>
    <option value="UA">UNITED ARAB EMIRATES</option>
    <option value="UK">UNITED KINGDOM</option>
    <option value="UY">URUGUAY</option>
    <option value="UZ">UZBEKISTAN</option>
    <option value="VU">VANUATU</option>
    <option value="VE">VENEZUELA</option>
    <option value="VN">VIETNAM</option>
    <option value="YE">YEMEN</option>
    <option value="YN">YEMEN, PEOPLES DEMOCRATIC REPUBLIC OF YEMEN</option>
    <option value="YO">YUGOSLAVIA</option>
    <option value="ZR">ZAIRE</option>
    <option value="ZA">ZAMBIA</option>
    <option value="ZM">ZIMBABWE</option>
    </select></div><span id="P130_CNTRY_error_placeholder" class="a-Form-error" data-template-id="76254838465060682_ET"></span></div></div><input type="hidden" id="P130_DATERANGE" name="P130_DATERANGE" value="N"><input type="hidden" id="P130_TITLE" name="P130_TITLE" value=" as of 05&#x2F;02&#x2F;2021"><input type="hidden" data-for="P130_TITLE" value="r17vq_d2xeaoUaOH1aR3zm4l3vMTMxfUku7OyvdaxC7cX3XFO6s0QnLwcGt04BljY-uFow4wRzKLCgEQTsOOOw">
        
    </div>
    <div class="t-Region-buttons t-Region-buttons--bottom">
        <div class="t-Region-buttons-left"></div>
        <div class="t-Region-buttons-right"></div>
    </div>
    </div>
    </div>
    <div class="t-Region t-Region--noPadding t-Region--scrollBody" id="R74911077795598754" >
    <div class="t-Region-header">
    <div class="t-Region-headerItems t-Region-headerItems--title">
        <h2 class="t-Region-title" id="R74911077795598754_heading">Number of Active Foreign Principals for<br>All Countries&#x2F;Locations  as of 05&#x2F;02&#x2F;2021 = <span class="highlight">     677</span><button onclick="apex.submit({request:&#x27;BACKQS&#x27;,validate:true});" class="t-Button t-Button--gapLeft" type="button"  id="B77387551850628701"><span class="t-Button-label">Back to Browse Filings</span></button></h2>
    </div>
    <div class="t-Region-headerItems t-Region-headerItems--buttons"><span class="js-maximizeButtonContainer"></span></div>
    </div>
    <div class="t-Region-bodyWrap">
    <div class="t-Region-buttons t-Region-buttons--top">
        <div class="t-Region-buttons-left"></div>
        <div class="t-Region-buttons-right"></div>
    </div>
    <div class="t-Region-body">
        
        
    <div id="R383217776904406575"  class="t-IRR-region " role="group" aria-labelledby="R383217776904406575_heading">
    <h2 class="u-VisuallyHidden" id="R383217776904406575_heading">     677 Active Foreign Principals for All Countries&#x2F;Locations  as of 05&#x2F;02&#x2F;2021</h2>
    <input type="hidden" id="P130_COUNTRY" name="P130_COUNTRY" value="All Countries&#x2F;Locations"><input type="hidden" data-for="P130_COUNTRY" value="ebSPHQ88ZESFPBBti2XPWbkTD52ABvnuPuhsSN50iqe5rhG9nITjY_nM6v2jQQ_GF6kw3juVdiLVepZeQmS5dg"><input type="hidden" id="P130_FP_NBR" name="P130_FP_NBR" value="     677"><div id="R383217776904406575_ir" class="a-IRR-container"><div id="R383217776904406575_worksheet_region" aria-live="polite"><div id="R383217776904406575_single_row_view" class="a-IRR-singleRowView"></div><div id="R383217776904406575_full_view" class="a-IRR-fullView"><div id="R383217776904406575_actions_menu"></div><div id="R383217776904406575_column_search_drop" class="a-IRR-colSearch"></div><div id="R383217776904406575_toolbar" class="a-IRR-toolbar"><div id="R383217776904406575_toolbar_controls" class="a-IRR-controls"><div class="a-IRR-controlGroup a-IRR-controlGroup--search"><div class="a-IRR-search"><input type="hidden" id="R383217776904406575_column_search_current_column" /><div class="a-IRR-colSelector"><button id="R383217776904406575_column_search_root" data-menu="R383217776904406575_column_search_drop" class="a-Button a-IRR-button a-IRR-button--colSearch js-menuButton" title="Select columns to search" aria-label="Select columns to search" type="button"><span class="a-Icon icon-search" aria-hidden="true"></span><span class="a-Icon icon-menu-drop-down" aria-hidden="true"></span></button></div><div class="a-IRR-searchFieldContainer"><input class="a-IRR-search-field" id="R383217776904406575_search_field" title="Search Report" type="text" size="30" maxlength="4000" value="" /></div><div class="a-IRR-searchButtonContainer"><button id="R383217776904406575_search_button" class="a-Button a-IRR-button a-IRR-button--search" type="button"  ><span>Go</span></button></div></div></div><div class="a-IRR-controlGroup a-IRR-controlGroup--views"></div><div class="a-IRR-controlGroup a-IRR-controlGroup--options"><input type="hidden" id="R383217776904406575_row_select" value="15" /><div class="a-IRR-actions"><button id="R383217776904406575_actions_button" class="a-Button a-IRR-button a-IRR-button--actions js-menuButton" type="button" data-menu="R383217776904406575_actions_menu">Actions<span class="a-Icon icon-menu-drop-down"></span></button></div></div></div></div><div id="R383217776904406575_content" class="a-IRR-content"><div id="R383217776904406575_dialog_js" class="a-IRR-dialogBody" style="display:none"></div><style id="R383217776904406575_worksheet_css" type="text/css">
    </style>
    <input type="hidden" id="R383217776904406575_worksheet_id" value="383217963674406575" />
    <input type="hidden" id="R383217776904406575_app_user" value="APEX_PUBLIC_USER" />
    <input type="hidden" id="R383217776904406575_report_id" value="383219258568406579" />
    <input type="hidden" id="R383217776904406575_view_mode" value="REPORT" />
    <div class="a-MediaBlock a-IRR-controlsContainer" id="R383217776904406575_control_panel"><div class="a-MediaBlock-graphic"><h3 class="u-VisuallyHidden">Report Settings</h3>
    <button type="button" class="a-Button a-IRR-button a-IRR-button--controls"></button>
    </div>
    <div class="a-MediaBlock-content">
    <ul class="a-IRR-controls">



    <li class="a-IRR-controls-item a-IRR-controls-item--controlBreak" role="group" aria-labelledby="control_text_COUNTRY_NAME"><span class="a-IRR-controls-cell"><input class="a-IRR-controlsCheckbox" data-setting="break" data-break-column="COUNTRY_NAME" type="checkbox" id="control_COUNTRY_NAME" checked="checked" /><label for="control_COUNTRY_NAME" class="a-IRR-controlsCheckboxLabel"><span class="u-VisuallyHidden">Toggle</span></label></span><span class="a-IRR-controls-cell"><span class="a-Icon a-IRR-controlsIcon icon-irr-control-break"></span></span><span class="a-IRR-controls-cell a-IRR-controls-cell--label"><a href="#" class="a-IRR-controlsLabel" data-setting="break"><span class="u-VisuallyHidden">Edit</span><span id="control_text_COUNTRY_NAME">Country&#x2F;Location Represented</span></a></span><span class="a-IRR-controls-cell a-IRR-controls-cell--remove"><button class="a-Button a-IRR-button a-Button--noUI a-IRR-button--remove" title="Remove Control Break" aria-label="Remove Control Break" type="button" data-setting="break" data-break-column="COUNTRY_NAME"><span class="a-Icon icon-remove" aria-hidden="true"></span></button></span></li>

    </ul>
    </div><div class="a-IRR-reportSummaryContainer" id="R383217776904406575_control_panel_summary"><ul class="a-IRR-reportSummary"><li class="a-IRR-reportSummary-item a-IRR-reportSummary-item--controlBreak"><a href="#" class="a-IRR-reportSummary-label" data-setting="break"><span class="a-IRR-reportSummary-icon"><span class="a-Icon icon-irr-control-break"></span></span><span class="a-IRR-reportSummary-value">Country&#x2F;Locatio...</span></a></li></ul></div></div><div id="R383217776904406575_chart" class="a-IRR-chartView"></div><div id="R383217776904406575_group_by" class="a-IRR-groupByView"></div><div id="R383217776904406575_pivot" class="a-IRR-pivotView"></div><div id="R383217776904406575_data_panel" class="a-IRR-reportView"><div class="a-IRR-tableContainer"><table summary="" class="a-IRR-table" id="383217963674406575">
    <tr><th colspan="8" class="a-IRR-header a-IRR-header--group" id="B77386298861628701_1">Country&#x2F;Location Represented : AFGHANISTAN</th></tr>
    <tr><th class="a-IRR-header u-tL" id="LINK"><span class="hideMeButHearMe">Link</span></th><th class="a-IRR-header u-tL" id="FP_NAME"><a class="a-IRR-headerLink" data-column="77385161203628698" href="#">Foreign Principal</a></th><th class="a-IRR-header u-tL" id="FP_REG_DATE"><a class="a-IRR-headerLink" data-column="77385481519628698" href="#">Foreign Principal<br>Registration Date</a></th><th class="a-IRR-header u-tL" id="ADDRESS_1"><a class="a-IRR-headerLink" data-column="77384293168628676" href="#">Address</a></th><th class="a-IRR-header u-tL" id="STATE"><a class="a-IRR-headerLink" data-column="77384741262628696" href="#">State</a></th><th class="a-IRR-header u-tL" id="REGISTRANT_NAME"><a class="a-IRR-headerLink" data-column="77383149545628657" href="#">Registrant</a></th><th class="a-IRR-header u-tL" id="REG_NUMBER"><a class="a-IRR-headerLink" data-column="77383558352628659" href="#">Registration #</a></th><th class="a-IRR-header u-tL" id="REG_DATE"><a class="a-IRR-headerLink" data-column="77383957466628676" href="#">Registration<br>Date</a></th></tr>

    <tr ><td headers="LINK B77386298861628701_1"><a href="f&#x3F;p&#x3D;1381&#x3A;200&#x3A;13701651723734&#x3A;&#x3A;NO&#x3A;RP,200&#x3A;P200_REG_NUMBER,P200_DOC_TYPE,P200_COUNTRY&#x3A;6504,Exhibit&#x25;20AB,AFGHANISTAN" ><img src="/i/view.gif" alt="View Documents"></a></td><td class=" u-tL" headers="FP_NAME B77386298861628701_1">Afghanistan-U.S. Democratic Peace and Prosperity Council, Inc.</td><td class=" u-tL" headers="FP_REG_DATE B77386298861628701_1">12/31/2020</td><td class=" u-tL" headers="ADDRESS_1 B77386298861628701_1">800 Maine Avenue,  SW<br>Washington&nbsp;&nbsp;20024</td><td class=" u-tL" headers="STATE B77386298861628701_1">DC</td><td class=" u-tL" headers="REGISTRANT_NAME B77386298861628701_1">Bullpen Strategy Group, Inc. </td><td class=" u-tC" headers="REG_NUMBER B77386298861628701_1">6504</td><td class=" u-tL" headers="REG_DATE B77386298861628701_1">12/29/2017</td></tr><tr ><td headers="LINK B77386298861628701_1"><a href="f&#x3F;p&#x3D;1381&#x3A;200&#x3A;13701651723734&#x3A;&#x3A;NO&#x3A;RP,200&#x3A;P200_REG_NUMBER,P200_DOC_TYPE,P200_COUNTRY&#x3A;6803,Exhibit&#x25;20AB,AFGHANISTAN" ><img src="/i/view.gif" alt="View Documents"></a></td><td class=" u-tL" headers="FP_NAME B77386298861628701_1">The Afghanistan - U.S. Democratic Peace and Prosperity Council</td><td class=" u-tL" headers="FP_REG_DATE B77386298861628701_1">03/19/2020</td><td class=" u-tL" headers="ADDRESS_1 B77386298861628701_1">3436 23rd Street, SE<br>Washington&nbsp;&nbsp;20020</td><td class=" u-tL" headers="STATE B77386298861628701_1">DC</td><td class=" u-tL" headers="REGISTRANT_NAME B77386298861628701_1">Wise Capital Strategy, LLC</td><td class=" u-tC" headers="REG_NUMBER B77386298861628701_1">6803</td><td class=" u-tL" headers="REG_DATE B77386298861628701_1">03/19/2020</td></tr><tr ><td headers="LINK B77386298861628701_1"><a href="f&#x3F;p&#x3D;1381&#x3A;200&#x3A;13701651723734&#x3A;&#x3A;NO&#x3A;RP,200&#x3A;P200_REG_NUMBER,P200_DOC_TYPE,P200_COUNTRY&#x3A;6817,Exhibit&#x25;20AB,AFGHANISTAN" ><img src="/i/view.gif" alt="View Documents"></a></td><td class=" u-tL" headers="FP_NAME B77386298861628701_1">Mohammed Gul Raoufi and other supporters of Afghanistan</td><td class=" u-tL" headers="FP_REG_DATE B77386298861628701_1">04/16/2020</td><td class=" u-tL" headers="ADDRESS_1 B77386298861628701_1">Qala-e-Najara, District 11,<br>Khairkharna, Kabul&nbsp;&nbsp;</td><td class=" u-tL" headers="STATE B77386298861628701_1"></td><td class=" u-tL" headers="REGISTRANT_NAME B77386298861628701_1">Afghanistan-U.S. Democratic Peace and Prosperity Council, Inc.</td><td class=" u-tC" headers="REG_NUMBER B77386298861628701_1">6817</td><td class=" u-tL" headers="REG_DATE B77386298861628701_1">04/16/2020</td></tr><tr ><td headers="LINK B77386298861628701_1"><a href="f&#x3F;p&#x3D;1381&#x3A;200&#x3A;13701651723734&#x3A;&#x3A;NO&#x3A;RP,200&#x3A;P200_REG_NUMBER,P200_DOC_TYPE,P200_COUNTRY&#x3A;6886,Exhibit&#x25;20AB,AFGHANISTAN" ><img src="/i/view.gif" alt="View Documents"></a></td><td class=" u-tL" headers="FP_NAME B77386298861628701_1">Afghanistan-U.S. Democratic Peace and Prosperity Council, Inc. (through Wise Capital Strategy LLC)</td><td class=" u-tL" headers="FP_REG_DATE B77386298861628701_1">11/03/2020</td><td class=" u-tL" headers="ADDRESS_1 B77386298861628701_1">800 Maine Ave. SW<br>Washington&nbsp;&nbsp;20024</td><td class=" u-tL" headers="STATE B77386298861628701_1">DC</td><td class=" u-tL" headers="REGISTRANT_NAME B77386298861628701_1">Jake Perry + Partners LLC</td><td class=" u-tC" headers="REG_NUMBER B77386298861628701_1">6886</td><td class=" u-tL" headers="REG_DATE B77386298861628701_1">11/03/2020</td></tr><tr ><td headers="LINK B77386298861628701_1"><a href="f&#x3F;p&#x3D;1381&#x3A;200&#x3A;13701651723734&#x3A;&#x3A;NO&#x3A;RP,200&#x3A;P200_REG_NUMBER,P200_DOC_TYPE,P200_COUNTRY&#x3A;6805,Exhibit&#x25;20AB,AFGHANISTAN" ><img src="/i/view.gif" alt="View Documents"></a></td><td class=" u-tL" headers="FP_NAME B77386298861628701_1">The Afghanistan-U.S. Democratic Peace and Properity Council</td><td class=" u-tL" headers="FP_REG_DATE B77386298861628701_1">03/20/2020</td><td class=" u-tL" headers="ADDRESS_1 B77386298861628701_1">3436 23rd Street, SE<br>Washington&nbsp;&nbsp;20020</td><td class=" u-tL" headers="STATE B77386298861628701_1">DC</td><td class=" u-tL" headers="REGISTRANT_NAME B77386298861628701_1">Duncap Strategies, LLC</td><td class=" u-tC" headers="REG_NUMBER B77386298861628701_1">6805</td><td class=" u-tL" headers="REG_DATE B77386298861628701_1">03/20/2020</td></tr><tr><th colspan="8" class="a-IRR-header a-IRR-header--group" id="B77386298861628701_2">Country&#x2F;Location Represented : ALBANIA</th></tr>
    <tr><th class="a-IRR-header u-tL" >&nbsp;</th><th class="a-IRR-header u-tL" ><span class="a-IRR-headerLabel">Foreign Principal</span></th><th class="a-IRR-header u-tL" ><span class="a-IRR-headerLabel">Foreign Principal<br>Registration Date</span></th><th class="a-IRR-header u-tL" ><span class="a-IRR-headerLabel">Address</span></th><th class="a-IRR-header u-tL" ><span class="a-IRR-headerLabel">State</span></th><th class="a-IRR-header u-tL" ><span class="a-IRR-headerLabel">Registrant</span></th><th class="a-IRR-header u-tL" ><span class="a-IRR-headerLabel">Registration #</span></th><th class="a-IRR-header u-tL" ><span class="a-IRR-headerLabel">Registration<br>Date</span></th></tr>
    <tr ><td headers="LINK B77386298861628701_2"><a href="f&#x3F;p&#x3D;1381&#x3A;200&#x3A;13701651723734&#x3A;&#x3A;NO&#x3A;RP,200&#x3A;P200_REG_NUMBER,P200_DOC_TYPE,P200_COUNTRY&#x3A;6399,Exhibit&#x25;20AB,ALBANIA" ><img src="/i/view.gif" alt="View Documents"></a></td><td class=" u-tL" headers="FP_NAME B77386298861628701_2">Democratic Party of Albania</td><td class=" u-tL" headers="FP_REG_DATE B77386298861628701_2">06/12/2018</td><td class=" u-tL" headers="ADDRESS_1 B77386298861628701_2">Bulevardi Zhan'dark 11<br>1000 Tirana&nbsp;&nbsp;</td><td class=" u-tL" headers="STATE B77386298861628701_2"></td><td class=" u-tL" headers="REGISTRANT_NAME B77386298861628701_2">Sonoran Policy Group, LLC</td><td class=" u-tC" headers="REG_NUMBER B77386298861628701_2">6399</td><td class=" u-tL" headers="REG_DATE B77386298861628701_2">12/11/2016</td></tr><tr><th colspan="8" class="a-IRR-header a-IRR-header--group" id="B77386298861628701_3">Country&#x2F;Location Represented : ALGERIA</th></tr>
    <tr><th class="a-IRR-header u-tL" >&nbsp;</th><th class="a-IRR-header u-tL" ><span class="a-IRR-headerLabel">Foreign Principal</span></th><th class="a-IRR-header u-tL" ><span class="a-IRR-headerLabel">Foreign Principal<br>Registration Date</span></th><th class="a-IRR-header u-tL" ><span class="a-IRR-headerLabel">Address</span></th><th class="a-IRR-header u-tL" ><span class="a-IRR-headerLabel">State</span></th><th class="a-IRR-header u-tL" ><span class="a-IRR-headerLabel">Registrant</span></th><th class="a-IRR-header u-tL" ><span class="a-IRR-headerLabel">Registration #</span></th><th class="a-IRR-header u-tL" ><span class="a-IRR-headerLabel">Registration<br>Date</span></th></tr>
    <tr ><td headers="LINK B77386298861628701_3"><a href="f&#x3F;p&#x3D;1381&#x3A;200&#x3A;13701651723734&#x3A;&#x3A;NO&#x3A;RP,200&#x3A;P200_REG_NUMBER,P200_DOC_TYPE,P200_COUNTRY&#x3A;6399,Exhibit&#x25;20AB,ALGERIA" ><img src="/i/view.gif" alt="View Documents"></a></td><td class=" u-tL" headers="FP_NAME B77386298861628701_3">Ali Hadad</td><td class=" u-tL" headers="FP_REG_DATE B77386298861628701_3">07/27/2020</td><td class=" u-tL" headers="ADDRESS_1 B77386298861628701_3">Care of Sabrina Run<br>63 Rue Pierre Charron 75008 Paris France&nbsp;&nbsp;</td><td class=" u-tL" headers="STATE B77386298861628701_3"></td><td class=" u-tL" headers="REGISTRANT_NAME B77386298861628701_3">Sonoran Policy Group, LLC</td><td class=" u-tC" headers="REG_NUMBER B77386298861628701_3">6399</td><td class=" u-tL" headers="REG_DATE B77386298861628701_3">12/11/2016</td></tr><tr ><td headers="LINK B77386298861628701_3"><a href="f&#x3F;p&#x3D;1381&#x3A;200&#x3A;13701651723734&#x3A;&#x3A;NO&#x3A;RP,200&#x3A;P200_REG_NUMBER,P200_DOC_TYPE,P200_COUNTRY&#x3A;4776,Exhibit&#x25;20AB,ALGERIA" ><img src="/i/view.gif" alt="View Documents"></a></td><td class=" u-tL" headers="FP_NAME B77386298861628701_3">Government of the People's Democratic Republic of Algeria, Embassy</td><td class=" u-tL" headers="FP_REG_DATE B77386298861628701_3">05/25/2007</td><td class=" u-tL" headers="ADDRESS_1 B77386298861628701_3">2118 Kalorama Road, NW<br>Washington&nbsp;&nbsp;20008</td><td class=" u-tL" headers="STATE B77386298861628701_3">DC</td><td class=" u-tL" headers="REGISTRANT_NAME B77386298861628701_3">Foley Hoag, LLP</td><td class=" u-tC" headers="REG_NUMBER B77386298861628701_3">4776</td><td class=" u-tL" headers="REG_DATE B77386298861628701_3">03/02/1993</td></tr><tr><th colspan="8" class="a-IRR-header a-IRR-header--group" id="B77386298861628701_4">Country&#x2F;Location Represented : ANGOLA</th></tr>
    <tr><th class="a-IRR-header u-tL" >&nbsp;</th><th class="a-IRR-header u-tL" ><span class="a-IRR-headerLabel">Foreign Principal</span></th><th class="a-IRR-header u-tL" ><span class="a-IRR-headerLabel">Foreign Principal<br>Registration Date</span></th><th class="a-IRR-header u-tL" ><span class="a-IRR-headerLabel">Address</span></th><th class="a-IRR-header u-tL" ><span class="a-IRR-headerLabel">State</span></th><th class="a-IRR-header u-tL" ><span class="a-IRR-headerLabel">Registrant</span></th><th class="a-IRR-header u-tL" ><span class="a-IRR-headerLabel">Registration #</span></th><th class="a-IRR-header u-tL" ><span class="a-IRR-headerLabel">Registration<br>Date</span></th></tr>
    <tr ><td headers="LINK B77386298861628701_4"><a href="f&#x3F;p&#x3D;1381&#x3A;200&#x3A;13701651723734&#x3A;&#x3A;NO&#x3A;RP,200&#x3A;P200_REG_NUMBER,P200_DOC_TYPE,P200_COUNTRY&#x3A;2165,Exhibit&#x25;20AB,ANGOLA" ><img src="/i/view.gif" alt="View Documents"></a></td><td class=" u-tL" headers="FP_NAME B77386298861628701_4">Republic of Angola</td><td class=" u-tL" headers="FP_REG_DATE B77386298861628701_4">06/25/2019</td><td class=" u-tL" headers="ADDRESS_1 B77386298861628701_4">Office of the Presidency of the Republic of Angola<br>Presidential Palace Luanda&nbsp;&nbsp;</td><td class=" u-tL" headers="STATE B77386298861628701_4"></td><td class=" u-tL" headers="REGISTRANT_NAME B77386298861628701_4">Squire Patton Boggs, LLP</td><td class=" u-tC" headers="REG_NUMBER B77386298861628701_4">2165</td><td class=" u-tL" headers="REG_DATE B77386298861628701_4">10/09/1969</td></tr><tr><th colspan="8" class="a-IRR-header a-IRR-header--group" id="B77386298861628701_5">Country&#x2F;Location Represented : ARGENTINA</th></tr>
    <tr><th class="a-IRR-header u-tL" >&nbsp;</th><th class="a-IRR-header u-tL" ><span class="a-IRR-headerLabel">Foreign Principal</span></th><th class="a-IRR-header u-tL" ><span class="a-IRR-headerLabel">Foreign Principal<br>Registration Date</span></th><th class="a-IRR-header u-tL" ><span class="a-IRR-headerLabel">Address</span></th><th class="a-IRR-header u-tL" ><span class="a-IRR-headerLabel">State</span></th><th class="a-IRR-header u-tL" ><span class="a-IRR-headerLabel">Registrant</span></th><th class="a-IRR-header u-tL" ><span class="a-IRR-headerLabel">Registration #</span></th><th class="a-IRR-header u-tL" ><span class="a-IRR-headerLabel">Registration<br>Date</span></th></tr>
    <tr ><td headers="LINK B77386298861628701_5"><a href="f&#x3F;p&#x3D;1381&#x3A;200&#x3A;13701651723734&#x3A;&#x3A;NO&#x3A;RP,200&#x3A;P200_REG_NUMBER,P200_DOC_TYPE,P200_COUNTRY&#x3A;1750,Exhibit&#x25;20AB,ARGENTINA" ><img src="/i/view.gif" alt="View Documents"></a></td><td class=" u-tL" headers="FP_NAME B77386298861628701_5">Embassy of the Republic of Argentina</td><td class=" u-tL" headers="FP_REG_DATE B77386298861628701_5">05/07/2020</td><td class=" u-tL" headers="ADDRESS_1 B77386298861628701_5">1600 New Hampshire Avenue, NW<br>Washington&nbsp;&nbsp;20009</td><td class=" u-tL" headers="STATE B77386298861628701_5">DC</td><td class=" u-tL" headers="REGISTRANT_NAME B77386298861628701_5">Arnold & Porter Kaye Scholer, LLP</td><td class=" u-tC" headers="REG_NUMBER B77386298861628701_5">1750</td><td class=" u-tL" headers="REG_DATE B77386298861628701_5">06/04/1964</td></tr><tr ><td headers="LINK B77386298861628701_5"><a href="f&#x3F;p&#x3D;1381&#x3A;200&#x3A;13701651723734&#x3A;&#x3A;NO&#x3A;RP,200&#x3A;P200_REG_NUMBER,P200_DOC_TYPE,P200_COUNTRY&#x3A;5666,Exhibit&#x25;20AB,ARGENTINA" ><img src="/i/view.gif" alt="View Documents"></a></td><td class=" u-tL" headers="FP_NAME B77386298861628701_5">Embassy of the Republic of Argentina</td><td class=" u-tL" headers="FP_REG_DATE B77386298861628701_5">05/04/2020</td><td class=" u-tL" headers="ADDRESS_1 B77386298861628701_5">1600 New Hampshire Ave.<br>Washington&nbsp;&nbsp;20009</td><td class=" u-tL" headers="STATE B77386298861628701_5">DC</td><td class=" u-tL" headers="REGISTRANT_NAME B77386298861628701_5">FGH Holdings</td><td class=" u-tC" headers="REG_NUMBER B77386298861628701_5">5666</td><td class=" u-tL" headers="REG_DATE B77386298861628701_5">01/31/2005</td></tr><tr ><td headers="LINK B77386298861628701_5"><a href="f&#x3F;p&#x3D;1381&#x3A;200&#x3A;13701651723734&#x3A;&#x3A;NO&#x3A;RP,200&#x3A;P200_REG_NUMBER,P200_DOC_TYPE,P200_COUNTRY&#x3A;6922,Exhibit&#x25;20AB,ARGENTINA" ><img src="/i/view.gif" alt="View Documents"></a></td><td class=" u-tL" headers="FP_NAME B77386298861628701_5">Embassy of the Republic of Argentina (on behalf of Arnold & Porter Kaye Scholer LLP)</td><td class=" u-tL" headers="FP_REG_DATE B77386298861628701_5">02/03/2021</td><td class=" u-tL" headers="ADDRESS_1 B77386298861628701_5">1600 New Hampshire Avenue, NW<br>Washington&nbsp;&nbsp;20009</td><td class=" u-tL" headers="STATE B77386298861628701_5">DC</td><td class=" u-tL" headers="REGISTRANT_NAME B77386298861628701_5">Ferox Strategies LLC</td><td class=" u-tC" headers="REG_NUMBER B77386298861628701_5">6922</td><td class=" u-tL" headers="REG_DATE B77386298861628701_5">02/03/2021</td></tr><tr><th colspan="8" class="a-IRR-header a-IRR-header--group" id="B77386298861628701_6">Country&#x2F;Location Represented : ARMENIA</th></tr>
    <tr><th class="a-IRR-header u-tL" >&nbsp;</th><th class="a-IRR-header u-tL" ><span class="a-IRR-headerLabel">Foreign Principal</span></th><th class="a-IRR-header u-tL" ><span class="a-IRR-headerLabel">Foreign Principal<br>Registration Date</span></th><th class="a-IRR-header u-tL" ><span class="a-IRR-headerLabel">Address</span></th><th class="a-IRR-header u-tL" ><span class="a-IRR-headerLabel">State</span></th><th class="a-IRR-header u-tL" ><span class="a-IRR-headerLabel">Registrant</span></th><th class="a-IRR-header u-tL" ><span class="a-IRR-headerLabel">Registration #</span></th><th class="a-IRR-header u-tL" ><span class="a-IRR-headerLabel">Registration<br>Date</span></th></tr>
    <tr ><td headers="LINK B77386298861628701_6"><a href="f&#x3F;p&#x3D;1381&#x3A;200&#x3A;13701651723734&#x3A;&#x3A;NO&#x3A;RP,200&#x3A;P200_REG_NUMBER,P200_DOC_TYPE,P200_COUNTRY&#x3A;6884,Exhibit&#x25;20AB,ARMENIA" ><img src="/i/view.gif" alt="View Documents"></a></td><td class=" u-tL" headers="FP_NAME B77386298861628701_6">Embassy of Armenia to the United States</td><td class=" u-tL" headers="FP_REG_DATE B77386298861628701_6">10/30/2020</td><td class=" u-tL" headers="ADDRESS_1 B77386298861628701_6">2225 R St NW<br>Washington&nbsp;&nbsp;20008</td><td class=" u-tL" headers="STATE B77386298861628701_6">DC</td><td class=" u-tL" headers="REGISTRANT_NAME B77386298861628701_6">Copper Strategies LLC</td><td class=" u-tC" headers="REG_NUMBER B77386298861628701_6">6884</td><td class=" u-tL" headers="REG_DATE B77386298861628701_6">10/30/2020</td></tr><tr><th colspan="8" class="a-IRR-header a-IRR-header--group" id="B77386298861628701_7">Country&#x2F;Location Represented : ARUBA</th></tr>
    <tr><th class="a-IRR-header u-tL" >&nbsp;</th><th class="a-IRR-header u-tL" ><span class="a-IRR-headerLabel">Foreign Principal</span></th><th class="a-IRR-header u-tL" ><span class="a-IRR-headerLabel">Foreign Principal<br>Registration Date</span></th><th class="a-IRR-header u-tL" ><span class="a-IRR-headerLabel">Address</span></th><th class="a-IRR-header u-tL" ><span class="a-IRR-headerLabel">State</span></th><th class="a-IRR-header u-tL" ><span class="a-IRR-headerLabel">Registrant</span></th><th class="a-IRR-header u-tL" ><span class="a-IRR-headerLabel">Registration #</span></th><th class="a-IRR-header u-tL" ><span class="a-IRR-headerLabel">Registration<br>Date</span></th></tr>
    <tr ><td headers="LINK B77386298861628701_7"><a href="f&#x3F;p&#x3D;1381&#x3A;200&#x3A;13701651723734&#x3A;&#x3A;NO&#x3A;RP,200&#x3A;P200_REG_NUMBER,P200_DOC_TYPE,P200_COUNTRY&#x3A;2987,Exhibit&#x25;20AB,ARUBA" ><img src="/i/view.gif" alt="View Documents"></a></td><td class=" u-tL" headers="FP_NAME B77386298861628701_7">Government of Aruba</td><td class=" u-tL" headers="FP_REG_DATE B77386298861628701_7">12/29/1978</td><td class=" u-tL" headers="ADDRESS_1 B77386298861628701_7">Oranjestad&nbsp;&nbsp;</td><td class=" u-tL" headers="STATE B77386298861628701_7"></td><td class=" u-tL" headers="REGISTRANT_NAME B77386298861628701_7">Aruba Tourism Authority</td><td class=" u-tC" headers="REG_NUMBER B77386298861628701_7">2987</td><td class=" u-tL" headers="REG_DATE B77386298861628701_7">12/29/1978</td></tr><tr ><td headers="LINK B77386298861628701_7"><a href="f&#x3F;p&#x3D;1381&#x3A;200&#x3A;13701651723734&#x3A;&#x3A;NO&#x3A;RP,200&#x3A;P200_REG_NUMBER,P200_DOC_TYPE,P200_COUNTRY&#x3A;6652,Exhibit&#x25;20AB,ARUBA" ><img src="/i/view.gif" alt="View Documents"></a></td><td class=" u-tL" headers="FP_NAME B77386298861628701_7">Aruba Tourism Authority (ATA)</td><td class=" u-tL" headers="FP_REG_DATE B77386298861628701_7">04/22/2019</td><td class=" u-tL" headers="ADDRESS_1 B77386298861628701_7">LG. Smith Blvd. 9 - P.O. Box 1019<br>Oranjestad&nbsp;&nbsp;</td><td class=" u-tL" headers="STATE B77386298861628701_7"></td><td class=" u-tL" headers="REGISTRANT_NAME B77386298861628701_7">Zeno Group, Inc.</td><td class=" u-tC" headers="REG_NUMBER B77386298861628701_7">6652</td><td class=" u-tL" headers="REG_DATE B77386298861628701_7">03/18/2019</td></tr></table></div><div class="a-IRR-paginationWrap a-IRR-paginationWrap--bottom"><ul class="a-IRR-pagination"><li aria-hidden="true" class="a-IRR-pagination-item is-disabled"></li><li class="a-IRR-pagination-item"><span class="a-IRR-pagination-label">1 - 15 of 677</span></li><li class="a-IRR-pagination-item"><button type="button" class="a-Button a-IRR-button a-IRR-button--pagination" aria-controls="R383217776904406575" title="Next" aria-label="Next" data-pagination="pgR_min_row=16max_rows=15rows_fetched=15"><span class="a-Icon icon-right-chevron" aria-hidden="true"></span></button></li></ul></div></div></div></div></div><div class="a-IRR-sortWidget" id="R383217776904406575_sort_widget" style="display:none;"><ul class="a-IRR-sortWidget-actions" id="R383217776904406575_sort_widget_actions"><li class="a-IRR-sortWidget-actions-item" id="R383217776904406575_sort_widget_action_up"><button class="a-Button a-IRR-button a-IRR-sortWidget-button" type="button" title="Sort Ascending" data-option="up"><span class="a-Icon icon-irr-sort-asc"></span></button></li><li class="a-IRR-sortWidget-actions-item" id="R383217776904406575_sort_widget_action_down"><button class="a-Button a-IRR-button a-IRR-sortWidget-button" type="button" title="Sort Descending" data-option="down"><span class="a-Icon icon-irr-sort-desc"></span></button></li><li class="a-IRR-sortWidget-actions-item" id="R383217776904406575_sort_widget_action_hide"><button class="a-Button a-IRR-button a-IRR-sortWidget-button" type="button" title="Hide Column" data-option="hide"><span class="a-Icon icon-irr-remove-col"></span></button></li><li class="a-IRR-sortWidget-actions-item" id="R383217776904406575_sort_widget_action_break"><button class="a-Button a-IRR-button a-IRR-sortWidget-button" type="button" title="Control Break" data-option="break"><span class="a-Icon icon-irr-control-break"></span></button></li><li class="a-IRR-sortWidget-actions-item" id="R383217776904406575_sort_widget_action_help"><button class="a-Button a-IRR-button a-IRR-sortWidget-button" type="button" title="Column Information" data-option="help"><span class="a-Icon icon-irr-help"></span></button></li><li class="a-IRR-sortWidget-actions-item" id="R383217776904406575_sort_widget_action_computation"><button class="a-Button a-IRR-button a-IRR-sortWidget-button" type="button" title="Compute" data-option="computation"><span class="a-Icon icon-irr-calculator"></span></button></li></ul><div class="a-IRR-sortWidget-help" id="R383217776904406575_sort_widget_help"></div><div class="a-IRR-sortWidget-search" id="R383217776904406575_sort_widget_search"><label for="R383217776904406575_sort_widget_search_field" class="a-IRR-sortWidget-searchLabel"><span class="u-VisuallyHidden">Search</span></label><input id="R383217776904406575_sort_widget_search_field" class="a-IRR-sortWidget-searchField" type="text" placeholder="Filter..." /><div class="a-IRR-sortWidget-rows" id="R383217776904406575_sort_widget_rows"></div></div></div></div>
    </div>

    </div>
    <div class="t-Region-buttons t-Region-buttons--bottom">
        <div class="t-Region-buttons-left"></div>
        <div class="t-Region-buttons-right"></div>
    </div>
    </div>
    </div>
    </center><table border="0"><tr><td colspan="2">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td><td></td></tr></table></TD>
            </TR>
            </TABLE>
                
                </center>
                </TD>
            
    </TR>
    <TR><TD></TD></TR>
    </TABLE>
    </center>

    </DIV></DIV></DIV></DIV>
    </ARTICLE>
    <input type="hidden" id="pPageItemsRowVersion" value="" /><input type="hidden" id="pPageItemsProtected" value="dKCTgRgeQpmtszMIZuxnT_pygI2uLElJnqSO-gqkFmk" /></form>


    <script type="text/javascript">
    var apex_img_dir = "/i/", htmldb_Img_Dir = apex_img_dir;
    </script>
    <!--[if lt IE 9]><script type="text/javascript" src="/i/libraries/jquery/1.12.3/jquery-1.12.3.min.js?v=5.1.2.00.09"></script><![endif]-->
    <!--[if gte IE 9]><!--><script type="text/javascript" src="/i/libraries/jquery/2.2.3/jquery-2.2.3.min.js?v=5.1.2.00.09"></script><!--<![endif]-->
    <script type="text/javascript" src="/i/libraries/apex/minified/desktop.min.js?v=5.1.2.00.09"></script>
    <script type="text/javascript" src="wwv_flow.js_messages?p_app_id=1381&p_lang=en&p_version=5.1.2.00.09-3146034050"></script>


    <script type="text/javascript" src="/i/libraries/hammer/2.0.4/hammer-2.0.4.min.js?v=5.1.2.00.09"></script>
    <script type="text/javascript" src="/i/libraries/apex/minified/widget.apexTabs.min.js?v=5.1.2.00.09"></script>
    <script type="text/javascript" src="/i/libraries/apex/minified/widget.stickyWidget.min.js?v=5.1.2.00.09"></script>
    <script type="text/javascript" src="/i/libraries/apex/minified/widget.stickyTableHeader.min.js?v=5.1.2.00.09"></script>
    <script type="text/javascript" src="/i/themes/theme_42/1.1/js/modernizr-custom.min.js?v=5.1.2.00.09"></script>
    <script type="text/javascript" src="/i/themes/theme_42/1.1/js/theme42.min.js?v=5.1.2.00.09"></script>



    
    <script type="text/javascript" src="/i/libraries/apex/minified/widget.interactiveReport.min.js?v=5.1.2.00.09"></script>
    <script type="text/javascript">
    apex.jQuery( document ).ready( function() {
    (function(){apex.widget.selectList("#P130_CNTRY",{"nullValue":"ALL","ajaxIdentifier":"MBt5sk36tGc39hpbQunNaYirXNAgPqRdDN1m6buPBftR23zoXO968bgp_cmYMnYe"});})();
    (function(){apex.jQuery('#R383217776904406575_ir').interactiveReport({"regionId":"R383217776904406575","toolbar":true,"searchField":true,"columnSearch":true,"rowsPerPageSelect":false,"reportsSelect":true,"actionsMenu":true,"reportViewMode":"REPORT","selectColumns":true,"filter":true,"rowsPerPage":true,"currentRowsPerPage":15,"maxRowsPerPage":"","maxRowCount":"500000","sort":true,"controlBreak":true,"highlight":false,"compute":false,"aggregate":false,"chart":false,"groupBy":true,"pivot":false,"flashback":false,"saveReport":false,"saveDefaultReport":false,"reset":true,"help":true,"helpLink":"wwv_flow_utilities.show_ir_help?p_app_id=1381\u0026p_worksheet_id=383217963674406575\u0026p_lang=en","download":true,"subscription":false,"pagination":true,"saveReportCategory":false,"detailLink":false,"isControlPanelCollapsed":false,"fixedHeader":"NONE","actionsMenuStructure":"IG","ajaxIdentifier":"5EXplKSaR7JiG5np0CApU6LVznt5zWzSiIfVJMPinvVM59SqAvNzajHT7_d_wJzk"});})();
    apex.theme42.initializePage.appLogin();

    apex.item( 'P130_CNTRY' ).setFocus();
    });</script>





                    </div>

            
        </div>
        <!-- /.l-main -->
        </div>
        <!-- /.l-main-wrapper -->
    </div>
    <!-- /.l-lower -->

    <div class="l-footer-wrapper">
        <footer class="l-footer" role="contentinfo">
            <div class="l-region l-region--footer">
        <nav id="block-menu-menu-footer-secondary-menu" role="navigation" class="block block--menu block--menu-menu-footer-secondary-menu">
            <h2 class="block__title">JUSTICE.GOV</h2>
        
    <ul class="menu"><li class="first expanded"><span title="" class="nolink">Third Column</span><ul class="menu"><li class="first leaf"><a href="https://www.justice.gov/grants" title="">Grants</a></li>
    <li class="leaf"><a href="https://www.justice.gov/business" title="">Business</a></li>
    <li class="leaf"><a href="http://www.justice.gov/forms" title="">Forms</a></li>
    <li class="leaf"><a href="https://www.justice.gov/publications" title="">Publications</a></li>
    <li class="last leaf"><a href="http://www.justice.gov/largecases/" title="Information for Victims in Large Cases">Information for Victims in Large Cases</a></li>
    </ul></li>
    <li class="expanded"><span class="nolink">Left Column</span><ul class="menu"><li class="first leaf"><a href="http://www.justice.gov/archive">Archive</a></li>
    <li class="leaf"><a href="https://www.justice.gov/accessibility/accessibility-information" title="">Accessibility</a></li>
    <li class="leaf"><a href="http://get.adobe.com/reader/otherversions/" title="">Adobe Reader</a></li>
    <li class="leaf"><a href="https://www.justice.gov/oip" title="">FOIA</a></li>
    <li class="leaf"><a href="https://www.justice.gov/jmd/eeo-program-status-report" title="">No FEAR Act</a></li>
    <li class="leaf"><a href="https://www.justice.gov/iqpr/information-quality" title="">Information Quality</a></li>
    <li class="leaf"><a href="https://www.justice.gov/doj/privacy-policy" title="">Privacy Policy</a></li>
    <li class="last leaf"><a href="https://www.justice.gov/legalpolicies" title="">Legal Policies &amp; Disclaimers</a></li>
    </ul></li>
    <li class="last expanded"><span class="nolink">Right Column</span><ul class="menu"><li class="first leaf"><a href="https://www.justice.gov/social" title="">Social Media</a></li>
    <li class="leaf"><a href="https://www.justice.gov/employees" title="">For Employees</a></li>
    <li class="leaf"><a href="http://www.justice.gov/oig">Office of the Inspector General</a></li>
    <li class="leaf"><a href="https://www.justice.gov/open" title="">Open Government</a></li>
    <li class="leaf"><a href="https://www.justice.gov/open/plain-writing-act" title="">Plain Writing</a></li>
    <li class="leaf"><a href="http://usa.gov">USA.gov</a></li>
    <li class="last leaf"><a href="http://business.usa.gov/">BusinessUSA</a></li>
    </ul></li>
    </ul></nav>
    <nav id="block-menu-menu-footer-menu-justice" role="navigation" class="block block--menu block--menu-menu-footer-menu-justice">
            <h2 class="block__title">Footer Menu Justice</h2>
        
    <ul class="menu"><li class="first expanded"><span title="" class="nolink">First Column</span><ul class="menu"><li class="first leaf"><a href="https://www.justice.gov/espanol" title="">en Español</a></li>
    <li class="leaf"><a href="https://www.justice.gov/contact-us" title="">Contact DOJ</a></li>
    <li class="last leaf"><a href="https://www.justice.gov/careers" title="">Careers</a></li>
    </ul></li>
    <li class="expanded"><span title="" class="nolink">Second Column</span><ul class="menu"><li class="first leaf"><a href="https://www.justice.gov/archive" title="">Archive</a></li>
    <li class="leaf"><a href="https://www.justice.gov/accessibility/accessibility-information" title="">Accessibility</a></li>
    <li class="leaf"><a href="https://www.justice.gov/iqpr/information-quality" title="">Information Quality</a></li>
    <li class="leaf"><a href="https://www.justice.gov/doj/privacy-policy" title="">Privacy Policy</a></li>
    <li class="leaf"><a href="https://www.justice.gov/legalpolicies" title="">Legal Policies &amp; Disclaimers</a></li>
    <li class="last leaf"><a href="https://www.justice.gov/social" title="">Social Media</a></li>
    </ul></li>
    <li class="last expanded"><span title="" class="nolink">Third Column</span><ul class="menu"><li class="first leaf"><a href="https://www.justice.gov/doj/budget-and-performance" title="">Budget &amp; Performance</a></li>
    <li class="leaf"><a href="https://oig.justice.gov/" title="">Office of the Inspector General</a></li>
    <li class="leaf"><a href="https://www.justice.gov/jmd/eeo-program-status-report" title="">No FEAR Act</a></li>
    <li class="leaf"><a href="https://www.justice.gov/employees" title="">For Employees</a></li>
    <li class="leaf"><a href="https://www.justice.gov/oip" title="">FOIA</a></li>
    <li class="last leaf"><a href="https://usa.gov" title="">USA.gov</a></li>
    </ul></li>
    </ul></nav>
    <div id="block-block-36" class="block block--block block--block-36">
            <div class="block__content">
        <div class="address">
    <h2>U.S. Department of Justice</h2>
    950 Pennsylvania Avenue, NW<br />
    Washington, DC 20530-0001</div>
    </div>
    </div>
    <div id="block-follow-site" class="block block--follow block--follow-site">
            <h2 class="block__title">Connect With Us</h2>
        <div class="block__content">
        <div class='follow-links clearfix site'><span class='follow-link-wrapper follow-link-wrapper-instagram'><a href="https://instagram.com/thejusticedept" class="follow-link follow-link-instagram follow-link-site" title="Follow us on Instagram">Instagram</a>
    </span><span class='follow-link-wrapper follow-link-wrapper-facebook'><a href="http://www.facebook.com/DOJ" class="follow-link follow-link-facebook follow-link-site" title="Follow us on Facebook">Facebook</a>
    </span><span class='follow-link-wrapper follow-link-wrapper-twitter'><a href="http://www.twitter.com/TheJusticeDept" class="follow-link follow-link-twitter follow-link-site" title="Follow us on Twitter">Twitter</a>
    </span><span class='follow-link-wrapper follow-link-wrapper-youtube'><a href="http://www.youtube.com/TheJusticeDepartment" class="follow-link follow-link-youtube follow-link-site" title="Follow us on YouTube">YouTube</a>
    </span></div>  </div>
    </div>
    <div id="block-block-26" class="block block--block block--block-26">
            <div class="block__content">
        <div class="update-title">
    <div class="title">
    <h2><a href="https://public.govdelivery.com/accounts/USDOJ/subscriber/new">Email Updates</a></h2>
    </div>

    <div class="email-logo"><a href="https://public.govdelivery.com/accounts/USDOJ/subscriber/new"><img alt="Email icon" src="fara_ws/r/1381/files/static/v17/email-icon.png" title="Follow us on Email" /></a></div>
    </div>
    </div>
    </div>
    </div>
        </footer>
    </div>
    </div>

    <script type="text/javascript" src="//ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
    <script type="text/javascript">
    <!--//--><![CDATA[//><!--
    window.jQuery||document.write("<script src='/sites/all/modules/contrib/jquery_update/replace/jquery/1.7/jquery.min.js'>\x3C/script>");
    //--><!]]>
    </script>
    <script type="text/javascript" src="https://www.justice.gov/sites/default/files/advagg_js/js__q0X56UwREcbJyzNybeawxQuz29PS0RVFWTYH2h61iGo__djjoHl6BGDusxBd2H_7L3zvUFs7u2nVqOwQ_6Uid4Ek__uTIQoWbf9AhTejt6tndAE72-EP5fOKFg8MdKnljcEMQ.js"></script>
    <script type="text/javascript" src="//ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js"></script>
    <script type="text/javascript">
    <!--//--><![CDATA[//><!--
    window.jQuery.ui||document.write("<script src='/sites/all/modules/contrib/jquery_update/replace/ui/ui/minified/jquery-ui.min.js'>\x3C/script>");
    //--><!]]>
    </script>
    <script type="text/javascript" src="https://www.justice.gov/sites/default/files/advagg_js/js__P2rLh1v2LkaimiTzQTjBZc1Vd2S--nSe5qfO4nPm4fI__7WJsicGBq887YQcKYBvGYsHw6HVr__II83PtyHK5WzA__uTIQoWbf9AhTejt6tndAE72-EP5fOKFg8MdKnljcEMQ.js"></script>
    <script type="text/javascript" src="https://www.justice.gov/sites/all/libraries/mediaelement/build/mediaelement-and-player.min.js?v=2.1.6"></script>
    <script type="text/javascript" src="https://www.justice.gov/sites/default/files/advagg_js/js__HeBlbfZg31W5-k3TnSu0psp6NxEebwWqfnnTeMENJc0__0pHO0iklafpAGQz1-symT5ZS590wnV0-uwvdq3VFa80__uTIQoWbf9AhTejt6tndAE72-EP5fOKFg8MdKnljcEMQ.js"></script>

    <!--[if (gte IE 6)&(lte IE 8)]>
    <script type="text/javascript" src="https://www.justice.gov/sites/default/files/advagg_js/js__UBTbecLPXcFRDNR3XjnGaFARkN87O-WXu18yLu6P1NE__YxqvutpREDoNXz22Aw7c17BIVoeHmcVG_xEpS91m3mU__uTIQoWbf9AhTejt6tndAE72-EP5fOKFg8MdKnljcEMQ.js"></script>
    <![endif]-->
    <script type="text/javascript" src="https://www.justice.gov/sites/default/files/advagg_js/js__b72Mq5iW2zyiAZHmW89LJXagLNN9aFfjHDJDywFfCEQ__gEXsVZiKPDn1DG_sW4TkOxh6Yb8hvoAY1D-HuEOa_uY__uTIQoWbf9AhTejt6tndAE72-EP5fOKFg8MdKnljcEMQ.js"></script>
    <script type="text/javascript">
    <!--//--><![CDATA[//><!--
    jQuery.extend(Drupal.settings,{"basePath":"\/","pathPrefix":"","autocomplete_limit":{"limit":2},"colorbox":{"transition":"none","speed":"350","opacity":"0.85","slideshow":true,"slideshowAuto":true,"slideshowSpeed":"6000","slideshowStart":"start slideshow","slideshowStop":"stop slideshow","current":"{current} of {total}","previous":"\u00ab Prev","next":"Next \u00bb","close":"Close","overlayClose":true,"returnFocus":true,"maxWidth":"98%","maxHeight":"98%","initialWidth":"300","initialHeight":"500","fixed":true,"scrolling":true,"mobiledetect":false,"mobiledevicewidth":"480px"},"nice_menus_options":{"delay":"800","speed":"fast"},"mediaelementAll":true,"better_exposed_filters":{"views":{"doj_banner":{"displays":{"block":{"filters":[]}}},"og_sidebar":{"displays":{"block":{"filters":[]}}}}},"responsive_menus":[{"selectors":".responsive .block--nice-menus .block__content, .responsive .l-region--navigation .block__content","container":"body","trigger_txt":"\u003Cspan \/\u003E\u003Cspan \/\u003E\u003Cspan \/\u003E","close_txt":"X","close_size":"18px","position":"right","media_size":"704","show_children":"1","expand_children":"1","expand_txt":"+","contract_txt":"-","remove_attrs":"1","responsive_menus_style":"mean_menu"}],"tablesorter":{"zebra":1,"odd":"odd","even":"even"},"extlink":{"extTarget":0,"extClass":"ext","extLabel":"(link is external)","extImgClass":0,"extSubdomains":1,"extExclude":"\\.(gov|mil|fed\\.us)(\\\/.*)?$","extInclude":"","extCssExclude":"","extCssExplicit":"","extAlert":"_blank","extAlertText":{"value":"The Department of Justice does not endorse the organizations or views represented by this site and takes no responsibility for, and exercises no control over, the accuracy, accessibility, copyright or trademark compliance or legality of the material contained on this site.\n\nThank you for visiting our site.","format":"full_html"},"mailtoClass":"mailto","mailtoLabel":"(link sends e-mail)"},"extlink_extra":{"extlink_alert_type":"colorbox","extlink_alert_type_colorbox_mobile":"confirm","extlink_alert_text_colorbox_mobile":"You are now leaving a Department of Justice Web site. You are about to access:\n\n[extlink:external-url]\n\nThe Department of Justice does not endorse the organizations or views represented by this site and takes no responsibility for, and exercises no control over, the accuracy, accessibility, copyright or trademark compliance or legality of the material contained on this site.\n\nThank you for visiting our site.","extlink_alert_timer":"4","extlink_alert_url":"\/pls\/apex\/wwv_flow_file_mgr.get_file?p_security_group_id=1044532716411962&p_fname=now-leaving.html","extlink_cache_fix":1,"extlink_exclude_warning":"","extlink_508_fix":1,"extlink_508_text":" [external link]","extlink_url_override":0,"extlink_url_params":{"external_url":null,"back_url":null}},"urlIsAjaxTrusted":{"https:\/\/search.justice.gov\/search":true},"ogContext":{"groupType":"node","gid":"1650"},"ajaxPageState":{"js":{"sites\/all\/modules\/contrib\/extlink_extra\/extlink_extra.js":1,"sites\/all\/modules\/contrib\/responsive_tables_filter\/tablesaw\/js\/tablesaw.stackonly.js":1,"sites\/all\/modules\/contrib\/responsive_tables_filter\/tablesaw\/js\/tablesaw-init.js":1,"sites\/all\/libraries\/jquery.event.move\/js\/jquery.event.move.js":1,"sites\/all\/libraries\/jquery.event.swipe\/js\/jquery.event.swipe.js":1,"sites\/all\/modules\/contrib\/colorbox_swipe\/colorbox_swipe.js":1,"\/\/ajax.googleapis.com\/ajax\/libs\/jquery\/1.7.2\/jquery.min.js":1,"misc\/jquery.once.js":1,"misc\/drupal.js":1,"sites\/all\/themes\/contrib\/omega\/omega\/js\/no-js.js":1,"sites\/all\/modules\/contrib\/jquery_update\/replace\/ui\/external\/jquery.cookie.js":1,"\/\/ajax.googleapis.com\/ajax\/libs\/jqueryui\/1.10.2\/jquery-ui.min.js":1,"sites\/all\/themes\/justice\/js\/justice.early-behaviors.js":1,"sites\/all\/modules\/contrib\/nice_menus\/js\/jquery.bgiframe.js":1,"sites\/all\/libraries\/jquery.hoverIntent\/jquery.hoverIntent.js":1,"sites\/all\/modules\/contrib\/nice_menus\/js\/superfish.js":1,"sites\/all\/modules\/contrib\/nice_menus\/js\/nice_menus.js":1,"sites\/all\/libraries\/mediaelement\/build\/mediaelement-and-player.min.js":1,"misc\/form.js":1,"sites\/all\/modules\/contrib\/tablesorter\/tablesortervar.js":1,"sites\/all\/modules\/contrib\/extlink\/extlink.js":1,"sites\/all\/themes\/justice\/libraries\/html5shiv\/html5shiv.min.js":1,"sites\/all\/themes\/justice\/libraries\/html5shiv\/html5shiv-printshiv.min.js":1,"sites\/all\/themes\/justice\/libraries\/selectivizr\/selectivizr.min.js":1,"sites\/all\/libraries\/colorbox\/jquery.colorbox-min.js":1,"sites\/all\/modules\/contrib\/colorbox\/js\/colorbox.js":1,"sites\/all\/modules\/contrib\/colorbox\/styles\/default\/colorbox_style.js":1,"sites\/all\/modules\/custom\/doj_analytics\/js\/doj_analytics_events.js":1,"sites\/all\/libraries\/mapify\/build\/jquery.mapify.js":1,"sites\/all\/modules\/contrib\/mediaelement\/mediaelement.js":1,"sites\/all\/modules\/features\/doj_image_map\/js\/doj_image_map_mapify.js":1,"sites\/all\/modules\/features\/doj_image_pane\/doj_image_pane.js":1,"sites\/all\/modules\/contrib\/responsive_menus\/styles\/meanMenu\/jquery.meanmenu.min.js":1,"sites\/all\/modules\/contrib\/responsive_menus\/styles\/meanMenu\/responsive_menus_mean_menu.js":1,"sites\/all\/libraries\/tablesorter\/jquery.tablesorter.min.js":1,"sites\/all\/libraries\/tablesorter\/jquery.metadata.js":1,"sites\/all\/libraries\/tablesorter\/addons\/pager\/jquery.tablesorter.pager.js":1,"misc\/collapse.js":1,"sites\/all\/modules\/features\/doj_sharing\/js\/doj_sharing.js":1,"sites\/all\/modules\/features\/doj_media\/js\/doj_media.colorbox.js":1,"sites\/all\/modules\/features\/doj_page_helpful\/js\/doj_page_helpful_was_helpful.js":1,"sites\/all\/modules\/features\/doj_shortcode\/js\/jumpmenu.js":1,"sites\/all\/themes\/justice\/js\/justice.behaviors.js":1}}});
    //--><!]]>
    </script>
    
    <script type="text/javascript">
    <!--//--><![CDATA[//><!--
    var usasearch_config={siteHandle:'justice'};
    //--><!]]>
    $("#apexir_rollover").appendTo("body");    
    </script>
    </body>
    </html>
"""