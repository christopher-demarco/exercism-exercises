(ns reverse-string)

(defn reverse-string
  [s]
  (reduce 
   (fn ([x y]
        (apply ; this is the key--apply str to each
         str   ; argument, and mash 'em together
         [y x] ; swapped of course
         )))
   
   "" ;; start reducing with at least two items
   
   (seq s))) ;; just dump the string as a list

