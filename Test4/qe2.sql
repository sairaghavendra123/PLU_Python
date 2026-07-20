create table student(
    StudentID INT PRIMARY KEY,
    Name VARCHAR(100),
    Course VARCHAR(50),
    Marks INT
);
insert into student values(101,'Rahul','Python',80);
insert into student values(102,'Priya','Java',75);
insert into student values(103,'Aman','Python',90);
insert into student values(104,'Neha','SQL',70);
select * from student;
select Name, Marks from student;
select Course from student;

