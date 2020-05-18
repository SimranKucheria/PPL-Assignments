(defun fact (n)
   (setq a 1)
   (loop for i from 1 to n
         do (setf a (* a i))
         finally (return a)))