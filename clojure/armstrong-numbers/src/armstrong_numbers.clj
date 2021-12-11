(ns armstrong-numbers)

(defn exp [base pow]
  (reduce * (repeat pow base)))

(defn armstrong? [num]
  (let [len (count num)]
    (reduce exp
           (seq (str num))
            
            
    

