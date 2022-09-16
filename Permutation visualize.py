
def indistinguishable_balls_in_bins(balls,bin_size):
  
   if not balls:
      yield len(bin_size) * (0,)

   elif len(bin_size) == 1:

 
      if bin_size[0] >= balls:
          yield (balls,)

   else:

     
      for balls_in_first_box in range( min(balls, bin_size[0]), -1, -1 ):
         balls_in_other_boxes= balls - balls_in_first_box

         for distribution_other in indistinguishable_balls_in_bins(
           balls_in_other_boxes, bin_size[1:]):

            if distribution_other[0] <= balls_in_first_box:
               yield (balls_in_first_box,) + distribution_other
               
list (indistinguishable_balls_in_bins(2,[1,1]))
print(indistinguishable_balls_in_bins(2,[1,1]))

def labeled_balls_in_unlabeled_boxes(balls, box_sizes):
   if not isinstance(balls, int):
      raise TypeError("balls must be a non-negative integer.")
   if balls < 0:
      raise ValueError("balls must be a non-negative integer.")

   if not isinstance(box_sizes, (list, tuple)):
      raise ValueError("box_sizes must be a non-empty list or tuple.")

   capacity= 0
   for size in box_sizes:
      if not isinstance(size, int):
          raise TypeError("box_sizes must contain only positive integers.")
      if size < 1:
          raise ValueError("box_sizes must contain only positive integers.")
      capacity+= size

   if capacity < balls:
      raise ValueError("The total capacity of the boxes is less than the "
        "number of balls to be distributed.")

   for unlabeled_dist in indistinguishable_balls_in_bins(balls, bin_sizes):
      for labeled_dist in \
        m_way_unordered_combinations(balls, unlabeled_dist):
         yield labeled_dist
         
         
