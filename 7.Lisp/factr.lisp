(defun factr(num)
	(if (= num 1) (return-from factr 1))
	(return-from factr (* num (factr (- num 1))))
)
(setq n (read))
(format t "factorial by recursion is: ~d ~%" (factr n))