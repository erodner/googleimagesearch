Google image downloader
=================================

Author: Erik Rodner (with code snipplets from the web)

First let ``gisapi.py`` download some URLs for the images

    python gisapi.py -q “traffic signs”

This creates a file ``out.json``, which contains information about the results

      {
            "content": "4-Way <b>Traffic Sign</b>", 
            "GsearchResultClass": "GimageSearch", 
            "visibleUrl": "www.emedco.com", 
            "titleNoFormatting": "4-Way Traffic Sign", 
            "originalContextUrl": "http://www.emedco.com/4-way-traffic-sign-rm227.html", 
            "unescapedUrl": "http://www.emedco.com/media/catalog/product/Traffic-Signs-RM227-ba.jpg", 
            "url": "http://www.emedco.com/media/catalog/product/Traffic-Signs-RM227-ba.jpg", 
            "title": "4-Way <b>Traffic Sign</b>", 
            "imageId": "ANd9GcSMEfJsoQdqmP1JRy2x5g-Acl7MQ7ZasIXXmMpcgIEHMM3eVUrRBb5Raw", 
            "height": "275", 
            "width": "275", 
            "tbUrl": "http://t3.gstatic.com/images?q=tbn:ANd9GcSMEfJsoQdqmP1JRy2x5g-Acl7MQ7ZasIXXmMpcgIEHMM3eVUrRBb5Raw", 
            "tbWidth": "114", 
            "contentNoFormatting": "4-Way Traffic Sign", 
            "tbHeight": "114"
        }

in JSON format. Afterwards you can download all the images with ``python img-downloader.py -j out.json -o trafficsigns/``, where ``trafficsigns/`` is a new destination directory.

Disclaimer: this is just a demonstration program and I take no responsibility for it's usage. Automatically scraping search results is for sure against some Google rules.

