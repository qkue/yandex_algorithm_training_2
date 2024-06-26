<div class="problem-statement">
   <div class="header">
      <h1 class="title">E. Автомобильные номера</h1>
      <table>
         <tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>2&nbsp;секунды</td>
         </tr>
         <tr class="memory-limit">
            <td class="property-title">Ограничение памяти</td>
            <td>64Mb</td>
         </tr>
         <tr class="input-file">
            <td class="property-title">Ввод</td>
            <td colspan="1">стандартный ввод или input.txt</td>
         </tr>
         <tr class="output-file">
            <td class="property-title">Вывод</td>
            <td colspan="1">стандартный вывод или output.txt</td>
         </tr>
      </table>
   </div>
   <h2></h2>
   <div class="legend"><span style="">
         <p>Неизвестный водитель совершил ДТП и скрылся с места происшествия. Полиция опрашивает свидетелей. Каждый из них говорит, что
            запомнил какие-то буквы и цифры номера. Но при этом свидетели не помнят порядок этих цифр и букв. Полиция хочет проверить
            несколько подозреваемых автомобилей. Будем говорить, что номер согласуется с показанием свидетеля, если все символы, которые
            назвал свидетель, присутствуют в этом номере (не важно, сколько раз).
         </p></span></div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Сначала задано число <span class="tex-math-inline"><img class="tex-math" src="pic1.png"></span> - количество свидетелей. Далее идет <span class="tex-math-text">M</span> строк, каждая из которых описывает показания очередного свидетеля. Эти строки непустые и состоят из не более чем 20 символов.
            Каждый символ в строке - либо цифра, либо заглавная латинская буква, причём символы могут повторяться. <br> 
         </p></span><p>Затем идёт число <span class="tex-math-inline"><img class="tex-math" src="pic2.png"></span> - количество номеров. Следующие строки представляют из себя номера подозреваемых машин и имеют такой же формат, как и показания
         свидетелей.
      </p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Выпишите номера автомобилей, согласующиеся с максимальным количеством свидетелей. Если таких номеров несколько, то выведите
            их в том же порядке, в котором они были заданы на входе.
         </p></span></div>
   <h3>Пример 1</h3>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td><pre>3
ABC
A37
BCDA
2
A317BD
B137AC
</pre></td>
            <td><pre>B137AC
</pre></td>
         </tr>
      </tbody>
   </table>
   <h3>Пример 2</h3>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td><pre>2
1ABC
3A4B
3
A143BC
C143AB
AAABC1
</pre></td>
            <td><pre>A143BC
C143AB
</pre></td>
         </tr>
      </tbody>
   </table>
</div></div>
