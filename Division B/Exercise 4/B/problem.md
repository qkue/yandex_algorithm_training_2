<div class="problem-statement">
   <div class="header">
      <h1 class="title">B. Выборы в США</h1>
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
         <p>Как известно, в США президент выбирается не прямым голосованием, а путем двухуровневого голосования. Сначала проводятся выборы
            в каждом штате и определяется победитель выборов в данном штате. Затем проводятся государственные выборы: на этих выборах
            каждый штат имеет определенное число голосов&nbsp;— число выборщиков от этого штата. На практике, все выборщики от штата голосуют
            в соответствии с результами голосования внутри штата, то есть на заключительной стадии выборов в голосовании участвуют штаты,
            имеющие различное число голосов. Вам известно за кого проголосовал каждый штат и сколько голосов было отдано данным штатом.
            Подведите итоги выборов: для каждого из участника голосования определите число отданных за него голосов. 
         </p></span></div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Каждая строка входного файла содержит фамилию кандидата, за которого отдают голоса выборщики этого штата, затем через пробел
            идет количество выборщиков, отдавших голоса за этого кандидата. 
         </p></span></div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Выведите фамилии всех кандидатов в лексикографическом порядке, затем, через пробел, количество отданных за них голосов. </p></span></div>
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
            <td><pre>McCain 10
McCain 5
Obama 9
Obama 8
McCain 1
</pre></td>
            <td><pre>McCain 16
Obama 17
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
            <td><pre>ivanov 100
ivanov 500
ivanov 300
petr 70
tourist 1
tourist 2
</pre></td>
            <td><pre>ivanov 900
petr 70
tourist 3
</pre></td>
         </tr>
      </tbody>
   </table>
   <h3>Пример 3</h3>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td><pre>bur 1
</pre></td>
            <td><pre>bur 1
</pre></td>
         </tr>
      </tbody>
   </table>
</div></div>
