(defun list-nth (N L)
  (if (null L)
      nil
    (if (zerop N) 
	(first L)
      (list-nth (- N 1) (rest L))))) 