# SOLID based on channels [EricRoby](https://www.youtube.com/watch?v=ZkknJI3QMss&ab_channel=EricRoby) 
Thứ nhất:  Single Responsibility Principle (S.R.P – nguyên lí đơn trách nhiệm): a class should have only a single responsibility. 1 class chỉ chịu một trách nhiệm/nhiệm vụ duy nhất.

Thứ 2: Open/Closed Principle (O.P.P – nguyên lí đóng mở): software entities … should be open for extension, but closed for modification. Một class, moldule, function… chỉ được phép mở rộng chứ không được sửa xóa

Thứ 3: Liskov Substitution principle (L.S.P – Nguyên lí thay thế Liskow): objects in a program should be replaceable with instances of their subtypes without altering the correctness of that program. Các đối tượng trong một chương trình có thể được thay thế bởi các class con mà không làm thay đổi tính đúng đắn của chương trình.

Thứ 4: Interface Segregation Principle (I.S.P – Nguyên lí phân biệt Interface): many client-specific interfaces are better than one general-purpose interface. Không nên sử dụng một interface lớn cho một mục đích chung, nên tách ra thành nhiều interface nhỏ với những mục đích cụ thể.

Cuối cùng: Dependency Inversion Principle (D.I.P – Nguyên lí nghịch đảo phụ thuộc): one should “depend upon abstractions, [not] concretions.”.