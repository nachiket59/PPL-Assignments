(defun fact(num)
	(defvar f 1)
	(loop for i from 1 to num do
		(setq f (* f i))
	)
	f
)
(setq n (read))

(format t "factorial by iteration is: ~d ~%" (fact n))
