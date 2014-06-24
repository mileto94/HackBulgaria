def unique_words_count(arr)
	count  = 1
	temp=Array.new()
	i = 0
	while  arr.size() > 0 && i <= arr.size()
		if arr.size() > temp.size()
			temp << arr[i] unless temp.include?(temp[i])
			arr -= temp
			count += 1
		end
		i+=1
	end
	return count
		
end
	
puts [unique_words_count(["apple", "banana", "apple", "pie"])]
puts [unique_words_count(["python", "python", "python", "ruby"])]
puts unique_words_count(['d','m','m','n','r','f','l','l'])