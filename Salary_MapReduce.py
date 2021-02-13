from mrjob.job import MRJob
from mrjob.step import MRStep

class MRAverage(MRJob):

    def mapper(self, _, lines):
        salaries = lines.split()
        for salary in salaries:
            yield None, '%05d'%int(salary)

    def reducer(self,key,values):
        self.list1 = []
        for value in values:
            self.list1.append(value)
        self.list2 = []
        for i in range(10):
            self.list2.append(max(self.list1))
            self.list1.remove(max(self.list1))
        for i in range(10):
            yield self.list2[i], None
              
if __name__ == '__main__':
    MRAverage.run()
