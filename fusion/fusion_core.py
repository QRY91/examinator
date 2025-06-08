#!/usr/bin/env python3
"""
EXAMINATOR FUSION MODE - Core Architecture
Democratizing AI-Assisted Education Through Constraint-Driven Innovation

Inspired by 100r's intermittent connectivity wisdom and Critical Engineering principles.
Local-first, cloud-augmented, bandwidth-conscious educational AI orchestration.
"""

import json
import hashlib
import time
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union
from dataclasses import dataclass, asdict
from enum import Enum
import gzip
import logging

# Configure logging for bandwidth-conscious environments
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class FusionMode(Enum):
    """Operating modes reflecting connectivity reality"""
    OFFLINE = "offline"           # Pure local operation
    UPLINK_PREP = "uplink_prep"   # Preparing for cloud sync
    UPLINK_SYNC = "uplink_sync"   # Active cloud synchronization
    CACHE_REFRESH = "cache_refresh" # Processing downloaded knowledge

@dataclass
class KnowledgeRequest:
    """Lightweight, bandwidth-optimized request structure"""
    request_id: str
    request_type: str  # "wiki_synthesis", "flashcard_batch", "concept_map"
    source_files: List[str]
    parameters: Dict
    priority: int  # 1-10, higher = more urgent
    created_at: datetime
    estimated_tokens: int
    
    def to_compressed_dict(self) -> Dict:
        """Minimize bandwidth usage"""
        return {
            'id': self.request_id,
            'type': self.request_type,
            'files': self.source_files,
            'params': self.parameters,
            'priority': self.priority,
            'tokens': self.estimated_tokens
        }

@dataclass
class KnowledgeCache:
    """Comprehensive, self-documenting cache entry"""
    cache_id: str
    request_id: str
    content_type: str
    content: str
    metadata: Dict
    created_at: datetime
    last_accessed: datetime
    access_count: int
    size_bytes: int
    
    def touch(self):
        """Update access tracking"""
        self.last_accessed = datetime.now()
        self.access_count += 1

class FusionCore:
    """
    Core orchestrator for intermittent AI-assisted education
    
    Philosophy: Design for disconnection, optimize for connection windows,
    cache comprehensively, degrade gracefully.
    """
    
    def __init__(self, base_path: str = "fusion"):
        self.base_path = Path(base_path)
        self.base_path.mkdir(exist_ok=True)
        
        # 100r-inspired directory structure
        self.cache_dir = self.base_path / "cache"
        self.queue_dir = self.base_path / "queue" 
        self.mirror_dir = self.base_path / "mirrors"
        self.logs_dir = self.base_path / "logs"
        
        for directory in [self.cache_dir, self.queue_dir, self.mirror_dir, self.logs_dir]:
            directory.mkdir(exist_ok=True)
            
        self.mode = FusionMode.OFFLINE
        self.bandwidth_budget = 0  # MB available for this session
        self.request_queue: List[KnowledgeRequest] = []
        self.cache_index: Dict[str, KnowledgeCache] = {}
        
        self._load_state()
        logger.info(f"🤖 FUSION CORE: Initialized in {self.mode.value} mode")
        
    def _load_state(self):
        """Load persistent state from disk"""
        try:
            # Load request queue
            queue_file = self.queue_dir / "pending_requests.json"
            if queue_file.exists():
                with open(queue_file, 'r') as f:
                    queue_data = json.load(f)
                    self.request_queue = [
                        KnowledgeRequest(**req) for req in queue_data
                    ]
            
            # Load cache index
            cache_index_file = self.cache_dir / "index.json"
            if cache_index_file.exists():
                with open(cache_index_file, 'r') as f:
                    index_data = json.load(f)
                    self.cache_index = {
                        k: KnowledgeCache(**v) for k, v in index_data.items()
                    }
                    
            logger.info(f"📂 Loaded {len(self.request_queue)} queued requests, {len(self.cache_index)} cached items")
            
        except Exception as e:
            logger.warning(f"⚠️ State loading failed: {e}")
            
    def _save_state(self):
        """Persist state to disk - critical for intermittent operation"""
        try:
            # Save request queue
            queue_file = self.queue_dir / "pending_requests.json"
            with open(queue_file, 'w') as f:
                queue_data = [asdict(req) for req in self.request_queue]
                json.dump(queue_data, f, indent=2, default=str)
            
            # Save cache index
            cache_index_file = self.cache_dir / "index.json"
            with open(cache_index_file, 'w') as f:
                index_data = {k: asdict(v) for k, v in self.cache_index.items()}
                json.dump(index_data, f, indent=2, default=str)
                
            logger.info("💾 State saved successfully")
            
        except Exception as e:
            logger.error(f"❌ State saving failed: {e}")

    def queue_synthesis_request(
        self, 
        source_files: List[str], 
        request_type: str = "wiki_synthesis",
        parameters: Optional[Dict] = None,
        priority: int = 5
    ) -> str:
        """
        Queue a knowledge synthesis request for next uplink window
        
        Following 100r principle: "Prior to connecting we make a list of tasks"
        """
        if parameters is None:
            parameters = {}
            
        # Generate deterministic ID for deduplication
        content_hash = hashlib.sha256(
            f"{request_type}:{':'.join(source_files)}:{json.dumps(parameters, sort_keys=True)}".encode()
        ).hexdigest()[:12]
        
        request_id = f"{request_type}_{content_hash}"
        
        # Check if already queued or cached
        if any(req.request_id == request_id for req in self.request_queue):
            logger.info(f"🔄 Request {request_id} already queued")
            return request_id
            
        if request_id in self.cache_index:
            logger.info(f"📚 Request {request_id} already cached")
            return request_id
        
        # Estimate token usage for bandwidth planning
        estimated_tokens = self._estimate_tokens(source_files)
        
        request = KnowledgeRequest(
            request_id=request_id,
            request_type=request_type,
            source_files=source_files,
            parameters=parameters,
            priority=priority,
            created_at=datetime.now(),
            estimated_tokens=estimated_tokens
        )
        
        self.request_queue.append(request)
        self.request_queue.sort(key=lambda x: x.priority, reverse=True)
        
        self._save_state()
        
        logger.info(f"📝 Queued {request_type} request: {request_id} ({estimated_tokens} tokens estimated)")
        return request_id
    
    def _estimate_tokens(self, source_files: List[str]) -> int:
        """Conservative token estimation for bandwidth planning"""
        total_chars = 0
        for file_path in source_files:
            try:
                with open(file_path, 'r') as f:
                    total_chars += len(f.read())
            except:
                total_chars += 5000  # Conservative fallback
        
        # Rough estimation: 4 chars per token, plus synthesis overhead
        return int(total_chars / 4 * 1.5)
    
    def prepare_uplink_session(self, bandwidth_budget_mb: float) -> Dict:
        """
        Prepare optimal batch for uplink window
        
        Following 100r bandwidth conservation: maximize educational value per MB
        """
        self.mode = FusionMode.UPLINK_PREP
        self.bandwidth_budget = bandwidth_budget_mb
        
        # Estimate bandwidth requirements
        selected_requests = []
        estimated_mb = 0
        
        for request in self.request_queue:
            # Conservative estimate: 1 token ≈ 1.5 bytes (request + response)
            request_mb = (request.estimated_tokens * 1.5) / (1024 * 1024)
            
            if estimated_mb + request_mb <= bandwidth_budget_mb:
                selected_requests.append(request)
                estimated_mb += request_mb
            else:
                break
                
        uplink_manifest = {
            'session_id': datetime.now().isoformat(),
            'mode': 'uplink_prep',
            'budget_mb': bandwidth_budget_mb,
            'estimated_usage_mb': estimated_mb,
            'selected_requests': len(selected_requests),
            'total_queued': len(self.request_queue),
            'requests': [req.to_compressed_dict() for req in selected_requests]
        }
        
        logger.info(f"🚀 Uplink session prepared: {len(selected_requests)} requests, ~{estimated_mb:.2f}MB")
        return uplink_manifest
    
    def cache_knowledge(
        self, 
        request_id: str, 
        content: str, 
        content_type: str = "wiki",
        metadata: Optional[Dict] = None
    ) -> bool:
        """
        Cache synthesized knowledge for offline access
        
        Inspired by 100r: "gather copies of all the online material we will need"
        """
        if metadata is None:
            metadata = {}
            
        # Compress large content
        if len(content) > 10000:  # 10KB threshold
            content_bytes = content.encode('utf-8')
            compressed = gzip.compress(content_bytes)
            
            if len(compressed) < len(content_bytes) * 0.8:  # 20% compression minimum
                content = compressed.hex()
                metadata['compressed'] = True
                logger.info(f"🗜️ Compressed content by {(1 - len(compressed)/len(content_bytes))*100:.1f}%")
        
        cache_entry = KnowledgeCache(
            cache_id=hashlib.sha256(f"{request_id}:{content_type}".encode()).hexdigest()[:12],
            request_id=request_id,
            content_type=content_type,
            content=content,
            metadata=metadata,
            created_at=datetime.now(),
            last_accessed=datetime.now(),
            access_count=0,
            size_bytes=len(content.encode('utf-8'))
        )
        
        # Save to disk
        cache_file = self.cache_dir / f"{cache_entry.cache_id}.json"
        with open(cache_file, 'w') as f:
            json.dump(asdict(cache_entry), f, indent=2, default=str)
        
        # Update index
        self.cache_index[request_id] = cache_entry
        
        # Remove from queue
        self.request_queue = [req for req in self.request_queue if req.request_id != request_id]
        
        self._save_state()
        
        logger.info(f"📚 Cached knowledge: {request_id} ({cache_entry.size_bytes} bytes)")
        return True
    
    def get_cached_knowledge(self, request_id: str) -> Optional[str]:
        """Retrieve cached knowledge with access tracking"""
        if request_id not in self.cache_index:
            return None
            
        cache_entry = self.cache_index[request_id]
        cache_entry.touch()
        
        # Load from disk if needed
        cache_file = self.cache_dir / f"{cache_entry.cache_id}.json"
        if cache_file.exists():
            with open(cache_file, 'r') as f:
                data = json.load(f)
                content = data['content']
                
                # Decompress if needed
                if data['metadata'].get('compressed', False):
                    content = gzip.decompress(bytes.fromhex(content)).decode('utf-8')
                
                logger.info(f"📖 Retrieved cached knowledge: {request_id}")
                return content
        
        return None
    
    def get_status(self) -> Dict:
        """Comprehensive status for monitoring and planning"""
        cache_size_mb = sum(entry.size_bytes for entry in self.cache_index.values()) / (1024 * 1024)
        
        return {
            'mode': self.mode.value,
            'queue': {
                'pending_requests': len(self.request_queue),
                'total_estimated_tokens': sum(req.estimated_tokens for req in self.request_queue),
                'high_priority': len([req for req in self.request_queue if req.priority >= 8])
            },
            'cache': {
                'total_entries': len(self.cache_index),
                'total_size_mb': round(cache_size_mb, 2),
                'most_accessed': max(self.cache_index.values(), key=lambda x: x.access_count).request_id if self.cache_index else None
            },
            'bandwidth_budget_mb': self.bandwidth_budget,
            'last_uplink': self._get_last_uplink_time()
        }
    
    def _get_last_uplink_time(self) -> Optional[str]:
        """Track uplink history for planning"""
        log_files = list(self.logs_dir.glob("uplink_*.log"))
        if log_files:
            latest = max(log_files, key=lambda x: x.stat().st_mtime)
            return datetime.fromtimestamp(latest.stat().st_mtime).isoformat()
        return None
    
    def cleanup_cache(self, max_age_days: int = 30, max_size_mb: int = 500):
        """
        Intelligent cache cleanup following 100r resource management principles
        """
        cutoff_date = datetime.now() - timedelta(days=max_age_days)
        current_size_mb = sum(entry.size_bytes for entry in self.cache_index.values()) / (1024 * 1024)
        
        if current_size_mb <= max_size_mb:
            logger.info(f"🧹 Cache cleanup: {current_size_mb:.1f}MB within limit")
            return
        
        # Sort by access patterns (LRU with access count consideration)
        sorted_entries = sorted(
            self.cache_index.items(),
            key=lambda x: (x[1].last_accessed, x[1].access_count)
        )
        
        cleaned_count = 0
        for request_id, entry in sorted_entries:
            if current_size_mb <= max_size_mb:
                break
                
            if entry.last_accessed < cutoff_date or entry.access_count == 0:
                # Remove cache file
                cache_file = self.cache_dir / f"{entry.cache_id}.json"
                if cache_file.exists():
                    cache_file.unlink()
                
                # Remove from index
                del self.cache_index[request_id]
                current_size_mb -= entry.size_bytes / (1024 * 1024)
                cleaned_count += 1
        
        self._save_state()
        logger.info(f"🧹 Cache cleanup: removed {cleaned_count} entries, {current_size_mb:.1f}MB remaining")

# CLI interface for fusion operations
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="🤖 EXAMINATOR FUSION MODE")
    parser.add_argument("--status", action="store_true", help="Show fusion status")
    parser.add_argument("--queue", nargs="+", help="Queue files for synthesis")
    parser.add_argument("--prepare-uplink", type=float, help="Prepare uplink session (MB budget)")
    parser.add_argument("--cleanup", action="store_true", help="Cleanup old cache entries")
    
    args = parser.parse_args()
    
    fusion = FusionCore()
    
    if args.status:
        status = fusion.get_status()
        print("🤖 EXAMINATOR FUSION STATUS:")
        print(f"  Mode: {status['mode']}")
        print(f"  Queued Requests: {status['queue']['pending_requests']}")
        print(f"  Cached Knowledge: {status['cache']['total_entries']} entries ({status['cache']['total_size_mb']}MB)")
        print(f"  Bandwidth Budget: {status['bandwidth_budget_mb']}MB")
    
    elif args.queue:
        request_id = fusion.queue_synthesis_request(
            source_files=args.queue,
            request_type="wiki_synthesis",
            priority=8
        )
        print(f"✅ Queued synthesis request: {request_id}")
    
    elif args.prepare_uplink:
        manifest = fusion.prepare_uplink_session(args.prepare_uplink)
        print(f"🚀 Uplink session prepared: {manifest['selected_requests']} requests (~{manifest['estimated_usage_mb']:.2f}MB)")
    
    elif args.cleanup:
        fusion.cleanup_cache()
        print("🧹 Cache cleanup completed")
    
    else:
        parser.print_help()