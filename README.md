## 目標
比較insertion sort, merge sort, 三種randomized quick sort (Lomuto Partition, Hoare Partition, 與3-Way Partition)與Counting sort。 

## 方法
測量三種array使用不同演算法的排序時間(實驗詳見pdf)。

## 結論
1.	insertion sort是O(n^2)，但在幾乎排序好的array(k小)時，排序的速度比merge sort、quick sort快，隨著array變亂(k增加)，insertion sort才會變得比較慢。
2.	Quick sort不同partition方法下，當元素大多相同時，執行時間三種方法差比較多，元素不同時，三種方法時間差不多。

