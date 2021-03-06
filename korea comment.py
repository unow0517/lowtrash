#!python

'''<!DOCTYPE html>
<html>
  <head>
   <meta charset='utf-8'>
   <link href="https://fonts.googleapis.com/css?family=Libre+Baskerville|Lobster&display=swap" rel="stylesheet">
    <meta charset='utf-8'>
    <title>쓰레기를 적게 만들자</title>
    <style>
        body{
           text-align: center;
        }
        li{
            font-size: 2rem;
        }
        h1{
          font-size:2rem; text-align:left; font-family: 'Lobster', cursive;
          position:fixed; left:0; top:0; width:100%; padding-left:10px;
          padding-top:5px; padding-bottom:5px; background-color:powderblue; margin:0;
        }
        .maker{
           text-align: right; position:fixed; width:98%; margin-top: -50px;
        }
        div{
            border:3px solid gray; margin: 0 5%;
            min-height:100px;
            font-size:1.7rem;
            }
        .cafe,.grocery,.textile,.recycle{
            display:grid;
            grid-template-columns: 33% 33% 33%;
            align-items: center;
            font-size: 2em;
        }
        a{
            text-decoration: none;
        }
    </style>
  </head>
  <body>
    <h1><strong>LOWTRASH</strong></h1>
    <p class='maker'><a href='why.html'>LOWTRASH?</a></p>
    <h2 style='margin-top:70px; text-align:center;'>LOWTRASH는 진심으로 환경을 생각하는 대한민국의 가게들을 모아놓은 웹사이트입니다.<br> 카페, 섬유, 식료품, 재활용 등 여러분야에서 활약하고 있는 친환경 가게들을 만나보실 수 있습니다.</h2>
        <li class='collapsible'>카페</li>
            <div class='cafe'>
                <a href="thepicker.html"><img src="thepicker.png" height=100 alt="더 피커 이미지"></a>

                <p id='bottlefactory'><a href="bottlefactory.html">Bottle Factory</a></p>

                <p id='earthus'><a href="earthus.html">Earth Us</a></p>

            </div>
        <li class='collapsible'>식료품</li>
            <a href="jigu.html"><div class='grocery'>
                제로웨이스트샵<br>'지구'
            </div></a>

        <li class = 'collapsible'>섬유</li>
            <div class='textile'>
                <a href="greenbliss.html"><img src="Greenbliss.png" height=80 alt="그린블리스"></a>
                <a href="000gan.html"><img src="korea%20textiles/000gan.png" alt=""></a>
            </div>

        <li class='collapsible'>재활용</li>
            <div class='recycle'>
                <a href="superbin.html"><img src="superbin.png" height=90 alt="수퍼빈"></a>
            </div>
        <h2>방명록</h2>
        <a href='create.py'>create</a>

    <script>
        var coll = document.getElementsByClassName('collapsible');
        var i

        for(i=0; i<coll.length; i++){
            coll[i].addEventListener('click',function(){
                this.classList.toggle("active");
                var content = this.nextElementSibling;
                if (content.style.display === 'block'){
                    content.style.display='none';
                } else {
                    content.style.display = 'grid';
                }
            });
        }
    </script>
  </body>
</html>'''
