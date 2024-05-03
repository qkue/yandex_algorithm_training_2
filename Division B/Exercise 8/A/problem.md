<div class="problem-statement">
   <div class="header">
      <h1 class="title">A. Бинарное дерево (вставка, поиск, обход)</h1>
      <table>
         <tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>1&nbsp;секунда</td>
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
         <p>Напишите программу, которая будет реализовывать действия в бинарном дереве поиска «вставить» и «найти» (по значению). Программа
            должна обрабатывать запросы трёх видов:
         </p></span><p>ADD n — если указанного числа еще нет в дереве, вставлять его и выводить слово «DONE», если уже есть — оставлять дерево как
         было и выводить слово «ALREADY».
      </p>
      <p>SEARCH — следует выводить слово «YES» (если значение найдено в дереве) или слово «NO» (если не найдено). Дерево при этом не
         меняется.
      </p>
      <p>PRINTTREE — выводить все дерево, обязательно используя алгоритм, указанный в формате вывода результатов.</p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>В каждой строке входных данных записан один из запросов ADD n или SEARCH n или PRINTTREE. Гарантируется, что запросы PRINTTREE
            будут вызываться только в моменты, когда дерево не пустое. Общее количество запросов не превышает 1000, из них не более 20
            запросов PRINTTREE.
         </p></span><p></p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Для каждого запроса выводите ответ на него. Для запросов ADD и SEARCH — соответствующее слово в отдельной строке. На запрос
            PRINTTREE надо выводить дерево, обязательно согласно такому алгоритму:
         </p></span><p>1) Распечатать левое поддерево</p>
      <p>2) Вывести количество точек, равное глубине узла</p>
      <p>3) Вывести значение ключа</p>
      <p>4) Распечатать правое поддерево </p>
   </div>
   <h2>Пример</h2>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td><pre>ADD 2
ADD 3
ADD 2
SEARCH 2
ADD 5
PRINTTREE
SEARCH 7
</pre></td>
            <td><pre>DONE
DONE
ALREADY
YES
DONE
2
.3
..5
NO
</pre></td>
         </tr>
      </tbody>
   </table>
</div></div>
