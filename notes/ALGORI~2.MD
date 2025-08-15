# Algorithm Sorting

Created: 17 March 2025 12:00
Class: 1
Is Completed: Yes

<aside>
📖

[https://read.kortext.com/reader/pdf/2361440/](https://read.kortext.com/reader/pdf/2361440/)

</aside>

LO1 - [Introduction to algorithm design](https://read.kortext.com/reader/pdf/1065493/C1)

## Insertion Sort

Start sorting from the second element.

Compare the current element with the element to its left.

If the current element is smaller, swap it with the left element.

Continue moving left until finding the correct position or reaching the start of the list.

Repeat this process until all elements are sorted.

- Processes one element at a time
- Efficiency depends on how well-sorted the data is initially

## Merge Sort

Merge Sort is a **divide-and-conquer** sorting algorithm that recursively **divides** an array into two halves, sorts each half, and then **merges** them back together in sorted order.

### **Steps of Merge Sort**

1. **Divide**: Split the array into two halves.
2. **Conquer**: Recursively sort both halves.
3. **Merge**: Combine the two sorted halves into a single sorted array.

## Problem Specification

Define the input and output.

Specify the allowed input instances and the expected output.

Key properties of an Algorithm:

Finiteness – Must always terminate with a solution.

Unambiguity – Steps must be clear and precise.

Sequence – Steps must follow a specific order to avoid errors or failures.

Feasibility – Must be executable within available resources (time, memory, computational power). For example, insertion sort works well for 10 elements but becomes inefficient for 1,000 elements.

## **Insertion Sort**

1. Start sorting from the second element (index 1).
2. Compare the current element with the element to its left.
3. If the current element is smaller, swap it.
4. Continue moving left until finding the correct position **or** reaching the list's start.
5. Repeat until all elements are sorted.

### **Key Characteristics:**

- Processes one element at a time.
- Efficiency varies based on how well the data is already sorted.

---

## **Merge Sort**

### **Problem Specification:**

- Define the input and output.
- Specify which input instances are allowed and what the expected output should be.

### **Key Properties of an Algorithm:**

- **Finiteness** – The algorithm must always terminate with a solution.
- **Unambiguity** – Each step must be clearly defined and unambiguous.
- **Sequence** – The steps must be executed in a specific order; changing the order could cause incorrect results or a failure.
- **Feasibility** – The algorithm must be executable within available resources (time, memory, computational power). For example, insertion sort is feasible for sorting 10 elements but becomes inefficient for sorting 1,000 elements.

> **How would you explain the difference between correctness and efficiency in an algorithm? Can you think of a scenario where one might be prioritised over the other?**Correctness ensures that an algorithm produces the right output for all valid inputs, while efficiency measures how well the algorithm uses resources like time or memory. For example, in safety-critical systems like aviation software, correctness is non-negotiable, even if the algorithm is slower. In contrast, for real-time applications like search engines, efficiency might take precedence as results need to be delivered almost instantaneously.**Consider the sorting problem. How might the choice of sorting algorithm change based on the size or type of data you are working with?**For small datasets, simpler algorithms like insertion sort might suffice due to their straightforward implementation. However, for large datasets, more efficient algorithms are preferred as they scale better with input size. Additionally, if the data is nearly sorted, insertion sort may perform exceptionally well compared to others.**How do you think the concept of generalisation applies to algorithms outside of sorting? Can you identify other tasks in everyday software applications where generalisation is crucial?**Generalisation ensures that an algorithm can handle a wide range of inputs and scenarios. Outside sorting, this is crucial for tasks like searching in databases (e.g., binary search) or navigating maps (e.g., Dijkstra's algorithm). For instance, a navigation app's algorithm must work for any geographic location and adjust dynamically for changing conditions like traffic.**Why is it important to consider the efficiency of an algorithm when developing software for real-time systems, such as air traffic control?**In real-time systems like air traffic control, it is crucial to consider the efficiency of algorithms because these systems require immediate responses to ensure safety and accuracy. Efficient algorithms can process data quickly and provide timely updates, which is essential for preventing collisions and managing air traffic smoothly.**How can the efficiency of an algorithm impact the scalability of a software application?**The efficiency of an algorithm directly affects the scalability of a software application. Efficient algorithms can handle increasing amounts of data or user requests without significant degradation in performance. This means that as the application grows and more users access it, the system remains responsive and performs well.**Why is it important to consider the feasibility of an algorithm before using it in real-world scenarios?**
Considering the feasibility of an algorithm is essential because it ensures the algorithm can be executed within practical time and resource limits. For example, Insertion Sort works well for small datasets but becomes impractical for large ones due to its time complexity. Choosing an appropriate algorithm based on its feasibility ensures efficiency and prevents resource exhaustion.**How does unambiguity affect the correctness of an algorithm?**
Unambiguity plays a critical role in ensuring the correctness of an algorithm. When an algorithm is unambiguous, each step is clearly defined with no room for interpretation. This means that every instruction can be followed without confusion, reducing the likelihood of errors. Ambiguity, on the other hand, introduces multiple possible interpretations of a single step, which can lead to different implementations of the algorithm. In such cases, different interpretations can result in incorrect outcomes or failures to solve the problem as intended.Furthermore, ambiguity complicates the process of proving the correctness of an algorithm. When the steps are unclear, it becomes much harder to reason through the algorithm and verify whether it will always produce the correct result. Proving that an algorithm is correct typically involves demonstrating that, for all possible inputs, the algorithm will eventually reach the desired output. This process relies on a clear and precise description of the steps involved. If the algorithm is ambiguous, it may be difficult, if not impossible, to establish a solid proof of correctness because the unclear steps could behave unpredictably in different scenarios. Therefore, unambiguity ensures that an algorithm is both reliably executable and provable as correct.**In the context of a university timetabling problem, what does correctness mean, and how would you ensure that the timetable you create is correct?**
Correctness in a university timetabling problem means ensuring that the schedule meets all specified requirements and constraints. For example, each class should be assigned a timeslot where it does not conflict with other classes, and professors should not be double-booked for classes that overlap. Additionally, students who enroll in multiple courses should not have scheduling conflicts between those courses. To ensure the timetable is correct, you would need to check for conflicts between classes, ensure all students' and faculty members' availability is respected, and make sure that resources like classrooms are allocated properly without any overlap. A correct timetable must also comply with any specific requirements, such as lab spaces being available for practical courses or specific timeslots for required cours
>