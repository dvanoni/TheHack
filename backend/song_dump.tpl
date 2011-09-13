<html>
<head>
<title>Song dump</title>
</head>

<body>
Songs retrieved are:
<br>
<div style="font-size:6pt">
<table>
  <tr>
    <th>Echonest ID</th>
    <th>7digital ID</th>
    <th>Title</th>
  </tr>
  %for song in songs:
    %for i in song:
    <tr>
      <td>{{song['id']}}</td>
      <td>{{song['tracks'][0]['foreign_id']}}</td>
      <td>{{song['title']}}</td>
    </tr>
    %end
  %end
</table> 
</div>

</body>

</html>
