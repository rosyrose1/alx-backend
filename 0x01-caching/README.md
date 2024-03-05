0x01. Caching

Resources
Read or watch:

Cache replacement policies - FIFO https://en.wikipedia.org/wiki/Cache_replacement_policies#First_In_First_Out_%28FIFO%29
Cache replacement policies - LIFO https://en.wikipedia.org/wiki/Cache_replacement_policies#Last_In_First_Out_%28LIFO%29
Cache replacement policies - LRU https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_Recently_Used_%28LRU%29
Cache replacement policies - MRU https://en.wikipedia.org/wiki/Cache_replacement_policies#Most_Recently_Used_%28MRU%29
Cache replacement policies - LFU https://en.wikipedia.org/wiki/Cache_replacement_policies#Least-Frequently_Used_%28LFU%29

General
What a caching system is
What FIFO means
What LIFO means
What LRU means
What MRU means
What LFU means
What the purpose of a caching system
What limits a caching system have

A caching system is a mechanism used in computing to store frequently accessed data in a temporary storage area called a cache. The purpose of caching is to improve data access time and system performance by reducing the need to retrieve data from the original source, such as a database or a remote server.

Here are some common caching policies:

FIFO (First-In, First-Out): In FIFO caching, the first item that was added to the cache is the first one to be removed when the cache reaches its capacity limit. It operates like a queue, where the oldest item is discarded to make room for new ones.

LIFO (Last-In, First-Out): In LIFO caching, the most recently added item to the cache is the first one to be removed when the cache reaches its capacity limit. It operates like a stack, where the newest item is removed first.

LRU (Least Recently Used): In LRU caching, the least recently used items are the first ones to be removed when the cache is full. This policy ensures that items that have not been accessed recently are replaced with newer ones.

MRU (Most Recently Used): In MRU caching, the most recently used items are the ones retained in the cache. When the cache reaches its capacity limit, the least recently used items are discarded to make room for new ones.

LFU (Least Frequently Used): In LFU caching, the least frequently used items are the first ones to be removed when the cache is full. This policy ensures that items that are accessed infrequently are replaced with more frequently accessed ones.

The purpose of a caching system is to improve performance by storing frequently accessed data closer to the point of use, reducing the time and resources required to retrieve the data from its original source. By caching data, systems can respond to user requests more quickly and efficiently.

However, caching systems have limitations:

Cache Size: Caches have finite storage capacity, so there's a limit to how much data can be cached. When the cache is full, older or less frequently accessed items may be evicted to make room for new ones, potentially leading to cache misses and decreased performance.

Cache Invalidation: Cached data may become outdated or stale over time, especially in systems where the original data is frequently updated. Ensuring that cached data remains consistent with the original source and managing cache invalidation can be challenging.

Cache Coherency: In distributed systems or systems with multiple cache layers, maintaining cache coherency—ensuring that all caches have consistent data—can be complex. Cache coherence protocols and mechanisms are used to address this issue.

Cache Warm-Up: Initially, caches may not contain the most frequently accessed data, leading to cache misses until the cache is warmed up. Strategies for cache warming, such as preloading frequently accessed data, can help mitigate this issue.

Cache Management Overhead: Managing caches adds computational overhead and complexity to the system. This includes cache eviction policies, cache invalidation mechanisms, and coordination between multiple cache layers. Efficient cache management strategies are essential to minimize overhead and maximize performance.





