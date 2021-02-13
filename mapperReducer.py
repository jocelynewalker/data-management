from mrjob.job import MRJob


class MRJobname(MRJob):
    def mapper(self, key, line):           
        line = line.strip(' ?.!,:()')           
        words = line.split()
        for word in words:                
            yield word.lower(), 1
    
    def reducer(self, word, occurrences):           
        yield word, sum(occurrences)
        
    if __name__ == '__main__':
        MRJobname.run()

