(ns app.core)

(defn p001
  []
  (- (+ (reduce + (range 3 1000 3))
        (reduce + (range 5 1000 5)))
     (reduce + (range 15 1000 15))))

(defn p002
  "return the sum of fibo numbers that satisfy f below lim"
  [lim f]
  (->> (iterate #(let [[a b] %] [b (+ a b)]) [0 1])
       (map first)
       (filter f)
       (take-while #(< % lim))
       (reduce +)))

