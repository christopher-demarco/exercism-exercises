(ns reverse-string)

(defn reverse-string
  "Return a string reversed, or the empty string if no input is given."
  ([s]
   (reduce 
    (fn ([x y]
         (apply ; this is the key--apply str to each
          str   ; argument, and mash 'em together
          [y x] ; swapped of course
          )))

    "" ;; start reducing with at least two items
    ;; any spare ""s are dropped from the final string

    (seq s))) ;; just dump the string as a list

  ;; if no input, return the empty string
  ([] (str)))
