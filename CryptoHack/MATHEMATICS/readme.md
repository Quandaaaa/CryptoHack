# Successive Powers
![alt text](<BRAINTEASERS PART 1/image/image.png>)
## Cách 1
Chall này cho ta một chuỗi lũy thừa liên tiếp trong modul $p$:<br>
$x^{n} = 588, x^{n+1} = 665, \dots$ <br>
$\to 588x \equiv 665\pmod p$ tương tự $665x \equiv 216\pmod p, \dots$ <br>

Đề cho ta biết rằng p là một số nguyên tố có 3 chữ số nên ta có thể bruforce được p. Ta chỉ cần chạy p từ 851 -> 999, nhưng mà chỉ cần xét các trường hợp số nguyên tố thui. <br>

Sử dụng CRT để tìm x với từng p brute-force. Nếu tồn tại x thì ta nhận cặp x và p làm flag. <br>

**Script:** [Successive_Powers.py](<BRAINTEASERS PART 1/Successive_Powers.py>)

## Cách 2
Cách này cần một chút quan sát :eyes: thoiiii. <br>

Mình sẽ lấy 2 cặp: <br>
$113x  \equiv 642 \pmod p$ và $114x  \equiv 851 \pmod p$

Suy ra: $x = 851 - 642 = 209$
Khi đã có x thì tìm p khá đơn giản 😙:.

<details>
<summary>FLAG</summary>

crypto{209,919}

</details>


