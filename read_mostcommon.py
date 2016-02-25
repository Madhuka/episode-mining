import csv
import sys
import operator
import os
import copy


#CSV methods sorting, listing, 

def csv_to_list(csv_file, delimiter=','):
    """ 
    Reads in a CSV file and returns the contents as list,
    where every row is stored as a sublist, and each element
    in the sublist represents 1 cell in the table.
    
    """
    with open(csv_file, 'r') as csv_con:
        reader = csv.reader(csv_con, delimiter=delimiter)
        return list(reader)
        
   
    
def print_csv(csv_content):
    """ Prints CSV file to standard output."""
    print(50*'-')
    for row in csv_content:
        row = [str(e) for e in row]
        print('\t'.join(row))
    print(50*'-')
    
def convert_cells_to_floats(csv_cont):
    """ 
    Converts cells to floats if possible
    (modifies input CSV content list).
    
    """
    for row in range(len(csv_cont)):
        for cell in range(len(csv_cont[row])):
            try:
                csv_cont[row][cell] = float(csv_cont[row][cell])
            except ValueError:
                pass 
                
def convert_cells_to_ints(csv_cont):
    """ 
    Converts cells to floats if possible
    (modifies input CSV content list).
    
    """
    for row in range(len(csv_cont)):
        for cell in range(len(csv_cont[row])):
            try:
                csv_cont[row][cell] = int(csv_cont[row][cell])
            except ValueError:
                pass 
                
def sort_by_column(csv_cont, col, reverse=False):
    """ 
    Sorts CSV contents by column name (if col argument is type <str>) 
    or column index (if col argument is type <int>). 
    
    """
    header = csv_cont[0]
    body = csv_cont[1:]
    if isinstance(col, str):  
        col_index = header.index(col)
    else:
        col_index = col
    body = sorted(body, 
           key=operator.itemgetter(col_index), 
           reverse=reverse)
    body.insert(0, header)
    return body
                  
def mark_minmax(csv_cont, col, mark_max=True, marker='*'):
    """
    Sorts a list of CSV contents by a particular column 
    (see sort_by_column function).
    Puts a marker on the maximum value if mark_max=True,
    or puts a marker on the minimum value mark_max=False
    (modifies input CSV content list).
    
    """
    
    sorted_csv = sort_by_column(csv_cont, col, reverse=mark_max)
    if isinstance(col, str):  
        col_index = sorted_csv[0].index(col)
    else:
        col_index = col
    sorted_csv[1][col_index] = str(sorted_csv[1][col_index]) + marker
    return None

    
def mark_all_col(csv_cont, mark_max=True, marker='*'):
    """
    Marks all maximum (if mark_max=True) or minimum (if mark_max=False)
    values in all columns of a CSV contents list - except the first column.
    Returns a new list that is sorted by the names in the first column
    (modifies input CSV content list).
    
    """

        
    for c in range(1, len(csv_cont[0])):
        mark_minmax(csv_cont, c, mark_max, marker)
    marked_csv = sort_by_column(csv_cont, 0, False)
    return marked_csv
    
def add_csv_col(csv_cont, col_name):
    """
    Marks all maximum (if mark_max=True) or minimum (if mark_max=False)
    values in all columns of a CSV contents list - except the first column.
    Returns a new list that is sorted by the names in the first column
    (modifies input CSV content list).
    
    """
    count =1
    header = csv_cont[0]
    body = csv_cont[1:]
    header.append(col_name)
    print header
    print len(body)
    for row in body:
        row.append(count)
        count +=1
    body.insert(0, header)
    print body
    return body
                
def write_csv(dest, csv_cont):
    """ Writes a comma-delimited CSV file. """

    with open(dest, 'w') as out_file:
        writer = csv.writer(out_file, delimiter=',')
        for row in csv_cont:
            writer.writerow(row)
            


def filter_csv_col(csv_cont, col_name, mapping_csv_cont):
    """
   updating csv file from col_name by looking on mapping csv file
    
    """

    count = 0
    header = csv_cont[0]
    body = csv_cont[1:]
    map_header = mapping_csv_cont[0]
    map_body = mapping_csv_cont[1:]
    size_map_body = len(map_body)

    current_old_id_col_name = "pageID"
    current_new_id_col_name = "newID"
    
    col_index = int(header.index(col_name))
    id_col_index = int(map_header.index(current_old_id_col_name))
    new_id_col_index = int(map_header.index(current_new_id_col_name))
    
    new_mapping_body = []
    for row in body:
        for i in range(count,size_map_body ):
            if int(map_body[i][id_col_index]) == int(row[col_index]):

                    new_mapping_body += [[i+1,row[1]]]

                    break
            
                
    new_mapping_body.insert(0, header)
    print new_mapping_body
    return new_mapping_body
#csv.field_size_limit(100000)
def filter2_csv_col(csv_cont, col_name, mapping_csv_cont):
    """
   updating csv file from session file with mapping new page IDs
    
    """

    count = 0
    header = csv_cont[0]
    body = csv_cont[1:]
    map_header = mapping_csv_cont[0]
    map_body = mapping_csv_cont[1:]
    size_map_body = len(map_body)
    print header
    current_old_id_col_name = "pageID"
    current_new_id_col_name = "newID"
    
    col_index = int(header.index(col_name))
    id_col_index = int(map_header.index(current_old_id_col_name))
    new_id_col_index = int(map_header.index(current_new_id_col_name))
    
    new_mapping_body = []
    Fout = []
    for row in body:
       # print row[1]
        data = row[1].split(",");
        SNo = row[0]
        print row
        if len(data)>=2:
            new_data=[]
            #print data
            for pageNo in data:
                for MpageNo in map_body:
                    if int(MpageNo[id_col_index]) == int(pageNo):
                      # new_data.append(MpageNo[id_col_index])
                        new_data += MpageNo[new_id_col_index]
            new_data.insert(0,SNo)
            Fout += [new_data]
            print new_data           
    Fout.insert(0, header)
    #print Fout
   # print new_mapping_body
    return Fout


def filter3_csv_col(csv_cont, col_name, mapping_csv_cont):
    """
   updating csv file from session file with mapping for clustering
    
    """

    count = 0
    header = csv_cont[0]
    body = csv_cont[1:]
    map_header = mapping_csv_cont[0]
    map_body = mapping_csv_cont[1:]
    size_map_body = len(map_body)
    print header
    current_old_id_col_name = "pageID"
    current_new_id_col_name = "newID"
    
    col_index = int(header.index(col_name))
    id_col_index = int(map_header.index(current_old_id_col_name))
    new_id_col_index = int(map_header.index(current_new_id_col_name))
    
    new_mapping_body = []
    Fout = []
    for row in body:
       # print row[1]
        data = row[1].split(",");
        SNo = row[0]
       
        if len(data)>=2:
            StrData = (101*"0")
            new_data = list(StrData)
            #print data
            for pageNo in data:
                for MpageNo in map_body:
                    if int(MpageNo[id_col_index]) == int(pageNo):
                      # new_data.append(MpageNo[id_col_index])
                        new_data[int(MpageNo[new_id_col_index])] = 1
            new_data.insert(0,SNo)
            Fout += [new_data]
            print new_data           
    Fout.insert(0, header)
    print Fout
   # print new_mapping_body
    return Fout


#end of csv method implemtation 

#CSV processing 

def process_csv(csv_in, csv_out):
    """ 
    Takes an input- and output-filename of an CSV file
    sort it and adding new pageID Col
    
    """
    csv_cont = csv_to_list(csv_in)
    csv_marked = copy.deepcopy(csv_cont)
    
    convert_cells_to_ints(csv_marked)
    csv_marked = sort_by_column(csv_marked, 'pageID')
    csv_marked = add_csv_col(csv_marked,"newID")
   # mark_all_col(csv_marked, mark_max=False, marker='*')
    write_csv(csv_out, csv_marked) 


def process2_csv(csv_in, csv_out,csv_map):

    csv_cont = csv_to_list(csv_in)
    csv_map = csv_to_list(csv_map)
    csv_marked = copy.deepcopy(csv_cont)
    csv_marked = filter2_csv_col(csv_marked,"mapping",csv_map)
    write_csv(csv_out, csv_marked) 
    
def process3_csv(csv_in, csv_out,csv_map):

    csv_cont = csv_to_list(csv_in)
    csv_map = csv_to_list(csv_map)
    csv_marked = copy.deepcopy(csv_cont)
    csv_marked = filter2_csv_col(csv_marked,"0",csv_map)
    write_csv(csv_out, csv_marked) 
    
def process4_csv(csv_in, csv_out,csv_map):

    csv_cont = csv_to_list(csv_in)
    csv_map = csv_to_list(csv_map)
    csv_marked = copy.deepcopy(csv_cont)
    csv_marked = filter3_csv_col(csv_marked,"0",csv_map)
    write_csv(csv_out, csv_marked) 


#End of CSV 
path = os.path.dirname(os.path.realpath(__file__))
#process_csv(path+"/mostcommon.csv",path+"/new_id.csv")
print ("processing 1 done.")

#process2_csv(path+"/mapping",path+"/new_mapping.csv",path+"/new_id.csv")
#process3_csv(path+"/sessionsfile",path+"/new_sessionsfile.csv",path+"/new_id.csv")
process4_csv(path+"/sessionsfile",path+"/new_cluster_sessionsfile.csv",path+"/new_id.csv")